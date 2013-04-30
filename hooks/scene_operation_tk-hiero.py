"""

"""
import os
import hiero

import tank
from tank import Hook
from tank import TankError

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
        if file_path:
            file_path = file_path.replace("/", os.path.sep)        
        
        if operation == "current_path":
            # return the current project path
            project = hiero.core.projects()[-1]
            return project.path()
        
        elif operation == "open":
            # open the specified project
            hiero.core.closeAllProjects(False)
            hiero.core.openProject(file_path)
            
        elif operation == "save":
            # save the current project
            project = hiero.core.projects()[-1]
            project.save()
            
        else:
            raise TankError("Don't know how to perform scene operation '%s'" % operation)