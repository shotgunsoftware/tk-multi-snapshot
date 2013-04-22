"""
Copyright (c) 2013 Shotgun Software, Inc
----------------------------------------------------

Multi Publish

"""

import os
import tank
from tank import TankError

class MultiSnapshot(tank.platform.Application):

    def init_app(self):
        """
        Called as the application is being initialized
        """
                
        tk_multi_snapshot = self.import_module("tk_multi_snapshot")
        self._handler = tk_multi_snapshot.Snapshot(self)
      
        # validate templates:
        work_template = self.get_template("template_work")
        snapshot_template = self.get_template("template_snapshot")
        
        # ensure snapshot template has at least one of increment or timestamp:
        if (not "timestamp" in snapshot_template.keys
            and not "increment" in snapshot_template.keys):
            self.log_error("'template_snapshot' must contain at least one of 'timestamp' or 'increment'")
            return
      
        # register commands:
        self.engine.register_command("Snapshot...", self._handler.show_snapshot_dlg)
        self.engine.register_command("Snapshot History...", self._handler.show_snapshot_history_dlg)
        
    def destroy_app(self):
        self.log_debug("Destroying tk-multi-snapshot")
        
    def snapshot(self, comment=None, thumbnail=None):
        """
        Snapshots the current scene without any UI
        """
        work_path = self._handler.get_current_file_path()
        self._handler.do_snapshot(work_path, thumbnail, comment)