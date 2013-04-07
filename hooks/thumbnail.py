"""
Copyright (c) 2013 Shotgun Software, Inc
----------------------------------------------------

"""
import tank
from tank import Hook

class ThumbnailHook(Hook):
    """
    Hook to scan scene for items to publish
    """
    def execute(self, engine_name, **kwargs):
        """
        Main hook entry point
        
        :engine_name:   String
                        The name of the engine the app is currently running
                        in
        
        :return:        String
                        Hook should return a file path pointing to the location of
                        a thumbnail file on disk that will be used for the snapshot.
                        If the hook returns None then the screenshot functionality
                        will be enabled in the UI.
        """
        
        # default implementation does nothing
        return None