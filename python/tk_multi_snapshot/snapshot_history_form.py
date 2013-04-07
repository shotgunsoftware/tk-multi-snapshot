"""
Copyright (c) 2013 Shotgun Software, Inc
----------------------------------------------------
"""
import os
import tank
from tank.platform.qt import QtCore, QtGui

class SnapshotHistoryForm(QtGui.QWidget):
    
    restore = QtCore.Signal(str)
    snapshot = QtCore.Signal()
    
    def __init__(self, app, handler, parent = None):
        QtGui.QWidget.__init__(self, parent)
    
        self._app = app
        self._handler = handler

        self._path = ""
    
        # set up the UI
        from .ui.snapshot_history_form import Ui_SnapshotHistoryForm
        self._ui = Ui_SnapshotHistoryForm()
        self._ui.setupUi(self)
        
        self._ui.snapshot_list.set_app(self._app)
        self._ui.snapshot_list.selection_changed.connect(self._on_list_selection_changed)
        
        self._ui.snapshot_list.action_requested.connect(self._on_restore)
        self._ui.restore_btn.clicked.connect(self._on_restore)
        
        self._ui.snapshot_btn.clicked.connect(self._on_snapshot_btn_clicked)
        
        self._update_ui()
    
    @property
    def path(self):
        return self._path
    @path.setter
    def path(self, value):
        if value != self._path:
            self._path = value
            file_name = os.path.basename(self._path)
            self._ui.snapshot_list.set_label(file_name)
            self._reload_history()
            
    def refresh(self):
        self._reload_history()
        
    def event(self, event):
        """
        override event to cause UI to reload the first time it is shown:
        """
        if event.type() == QtCore.QEvent.Polish:
            self._reload_history()
        return QtGui.QWidget.event(self, event)

    def _on_list_selection_changed(self):
        self._update_ui()
        
    def _on_restore(self):
        path = self._ui.snapshot_list.get_selected_path()
        self.restore.emit(path)
        
    def _on_snapshot_btn_clicked(self):
        self.snapshot.emit()
        
    def _reload_history(self):
        self._ui.snapshot_list.clear()
        self._ui.snapshot_list.load({"handler":self._handler,
                                     "file_path":self._path})
        
    def _update_ui(self):
        can_restore = self._ui.snapshot_list.get_selected_item() != None
        self._ui.restore_btn.setEnabled(can_restore)
        


    