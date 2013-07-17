"""
Copyright (c) 2013 Shotgun Software, Inc
----------------------------------------------------

"""
import os

import tank
from tank import Hook

import win32com
from win32com.client import Dispatch, constants
from pywintypes import com_error

Application = Dispatch("XSI.Application").Application

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
                    'reset'        - True if scene was reset to an empty 
                                     state, otherwise False
                    all others     - None
        """
        
        if operation == "current_path":
            # return the current scene path
            
            # query the current scene 'name' and file path from the application:
            scene_filepath = Application.ActiveProject.ActiveScene.filename.value
            scene_name = Application.ActiveProject.ActiveScene.Name
                        
            # There doesn't seem to be an easy way to determin if the current scene 
            # is 'new'.  However, if the file name is "Untitled.scn" and the scene 
            # name is "Scene" rather than "Untitled", then we can be reasonably sure 
            # that we haven't opened a file called Untitled.scn
            if scene_name == "Scene" and os.path.basename(scene_filepath) == "Untitled.scn":
                return ""
            return scene_filepath

        elif operation == "open":
            # open the specified scene without any prompts
            # Application.OpenScene(path, Confirm, ApplyAuxiliaryData)
            Application.OpenScene(file_path, False, False)

        elif operation == "save":
            # save the current scene:
            Application.SaveScene()

        elif operation == "reset":
            # reset the scene to an empty state
            try:
                # The standard Softimage mechanism will check
                # for and save the file if required
                # Application.NewScene(project_path, Confirm)
                Application.NewScene("", True)
            except com_error:
                # exception here means the user hit 'Cancel'
                return False
            else:
                return True
            
            
            
            
