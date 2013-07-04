"""
Copyright (c) 2013 Shotgun Software, Inc
----------------------------------------------------

"""
import os
import hou

import tank
from tank import Hook
from tank import TankError


class SceneOperation(Hook):
    """
    Hook called to perform an operation with the current scene
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
            return str(hou.hipFile.name())
        elif operation == "open":
            # give houdini forward slashes
            file_path = file_path.replace(os.path.sep, '/')
            hou.hipFile.load(str(file_path))
        elif operation == "save":
            hou.hipFile.save()
        else:
            raise TankError("Don't know how to perform scene operation '%s'" % operation)
