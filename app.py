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
      
        # validate templates:
        work_template = self.get_template("template_work")
        snapshot_template = self.get_template("template_snapshot")
        
        # ensure snapshot template has at least one of increment or timestamp:
        if (not "timestamp" in snapshot_template.keys
            and not "increment" in snapshot_template.keys):
            self.log_error("'template_snapshot' must contain at least one of 'timestamp' or 'increment'")
            return
      
        # register commands:
        cmd = lambda app=self: tk_multi_snapshot.Snapshot.show_snapshot_dlg(app)
        self.engine.register_command("Snapshot...", cmd)
        
        cmd = lambda app=self: tk_multi_snapshot.Snapshot.show_snapshot_history_dlg(app)
        self.engine.register_command("Snapshot History...", cmd)
        
    def destroy_app(self):
        self.log_debug("Destroying tk-multi-snapshot")