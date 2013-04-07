"""
Copyright (c) 2013 Shotgun Software, Inc
----------------------------------------------------
"""

import tank
from tank.platform.qt import QtGui, QtCore

browser_widget = tank.platform.import_framework("tk-framework-widget", "browser_widget")

class SnapshotItem(browser_widget.ListItem):
    """
    Extend ListItem to provide additional functionality for a snapshot
    """
    def __init__(self, app, worker, parent = None):
        browser_widget.ListItem.__init__(self, app, worker, parent)
    
        self._path = ""
        
        # tweak UI size:
        #self.geometry()
        
    @property
    def path(self):
        """
        Property contains the file path for the snapshot
        it represents
        """
        return self._path
    @path.setter
    def path(self, value):
        self._path = value
        
        
        
    
    