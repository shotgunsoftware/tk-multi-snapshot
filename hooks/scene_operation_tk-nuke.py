"""
Copyright (c) 2013 Shotgun Software, Inc
----------------------------------------------------

"""
import os
import nuke

import tank
from tank import Hook

class SceneOperation(Hook):
    """
    Hook called to perform an operation with the 
    current scene
    """
    
    def execute(self, operation, file_path, **kwargs):
        """
        Main hook entry point
        
        :operation: String
                    Scene operation to perform
        
        :file_path: String
                    File path to use if the operation
                    requires it (e.g. open)
                    
        :returns:   Depends on operation:
                    'current_path' - Return the current scene
                                     file path as a String
                    all others     - None
        """
        
        if operation == "current_path":
            # return the current script path
            return nuke.root().name().replace("/", os.path.sep)
        elif operation == "open":
            # open the specified script
            nuke.scriptOpen(file_path)
        elif operation == "save":
            # save the current script:
            nuke.scriptSave()
        else:
            raise Exception("Don't know how to perform scene operation '%s'" % operation)