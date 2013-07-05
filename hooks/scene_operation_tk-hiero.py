"""
Copyright (c) 2013 Shotgun Software, Inc
----------------------------------------------------

"""
import os
import hiero.core

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
            project = self._get_current_project()
            curr_path = project.path().replace("/", os.path.sep)
            return curr_path
        
        elif operation == "open":
            # first close the current project then open the specified file 
            project = self._get_current_project()
            project.close()
            hiero.core.openProject(file_path)

        elif operation == "save":
            # save the current script:
            project = self._get_current_project()
            project.save()        


    def _get_current_project(self):
        """
        Returns the current project based on where in the UI the user clicked 
        """
        
        # get the menu selection from hiero engine
        selection = self.parent.engine.get_menu_selection()

        if len(selection) != 1:
            raise Exception("Please select a single Project!")
        
        if not isinstance(selection[0] , hiero.core.Bin):
            raise Exception("Please select a Hiero Project!")
            
        project = selection[0].project()
        if project is None:
            # apparently bins can be without projects (child bins I think)
            raise Exception("Please select a Hiero Project!")
        
        return project
