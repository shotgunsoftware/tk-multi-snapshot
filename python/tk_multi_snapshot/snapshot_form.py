"""
Copyright (c) 2013 Shotgun Software, Inc
----------------------------------------------------
"""
import tank
from tank.platform.qt import QtCore, QtGui

thumbnail_widget = tank.platform.import_framework("tk-framework-widget", "thumbnail_widget")

class ThumbnailWidget(thumbnail_widget.ThumbnailWidget):
    pass

class SnapshotForm(QtGui.QWidget):
    """
    Main snapshot UI
    """
    
    # signal emitted when user clicks the 'Create Snapshot' button
    snapshot = QtCore.Signal(QtGui.QWidget, str)
    
    SHOW_HISTORY_RETURN_CODE = 2
    
    def __init__(self, file_path, thumbnail, setup_cb, parent = None):
        """
        Construction
        """
        QtGui.QWidget.__init__(self, parent)
    
        self._path = file_path
    
        # set up the UI
        from .ui.snapshot_form import Ui_SnapshotForm
        self._ui = Ui_SnapshotForm()
        self._ui.setupUi(self)

        self.thumbnail = thumbnail
        self._exit_code = QtGui.QDialog.Rejected

        self._ui.snapshot_btn.clicked.connect(self._on_do_snapshot)        
        self._ui.cancel_btn.clicked.connect(self._on_do_cancel)
        self._ui.close_btn.clicked.connect(self._on_do_close)
        self._ui.history_btn.clicked.connect(self._on_show_history)

        # ensure snapshot page is shown first:
        self._ui.page_stack.setCurrentWidget(self._ui.snapshot_page)
        
        # finally, run setup callback to allow caller to connect 
        # up signals etc.
        setup_cb(self)
            
    @property
    def exit_code(self):
        return self._exit_code
    
    @property
    def thumbnail(self):
        return self._ui.thumbnail_widget.thumbnail
    @thumbnail.setter
    def thumbnail(self, value):
        self._ui.thumbnail_widget.thumbnail = value
    
    @property
    def comment(self):
        return self._ui.comment_edit.toPlainText().rstrip()
    @comment.setter
    def comment(self, value):
        self._ui.comment_edit.setPlainText(value)
        
    def show_result(self, status, msg):
        """
        Show the result page
        """
        self._ui.page_stack.setCurrentWidget(self._ui.status_page)
        self._ui.status_title.setText(["Oh No, Something Went Wrong!", "Success!"][status])
        self._ui.status_details.setText([msg, "Snapshot Successfully Created"][not msg])
        self._ui.status_icon.setPixmap(QtGui.QPixmap([":/res/failure.png", ":/res/success.png"][status]))
        
    def _on_do_cancel(self):
        self._exit_code = QtGui.QDialog.Rejected
        self.close()

    def _on_do_close(self):
        self._exit_code = QtGui.QDialog.Accepted
        self.close()
    
    def _on_do_snapshot(self):
        # emit signal to do snapshot:
        self.snapshot.emit(self, self._path)    
        
    def _on_show_history(self):
        self._exit_code = SnapshotForm.SHOW_HISTORY_RETURN_CODE
        self.close()
                
    