"""
Copyright (c) 2013 Shotgun Software, Inc
----------------------------------------------------

"""
import os
import c4d

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
        if operation == "current_path":
            # return the current scene path
            doc = c4d.documents.GetActiveDocument()
            scene_path = os.path.join(doc.GetDocumentPath(),doc.GetDocumentName())
            return scene_path
        elif operation == "open":
            # open the file            
            c4d.documents.LoadFile(file_path)
        elif operation == "save":
            # save the current scene:
            doc = c4d.documents.GetActiveDocument()
            scene_path = os.path.join(doc.GetDocumentPath(),doc.GetDocumentName())
            c4d.documents.SaveDocument(doc, scene_path, c4d.SAVEDOCUMENTFLAGS_0, c4d.FORMAT_C4DEXPORT)
        else:
            raise TankError("Don't know how to perform scene operation '%s'" % operation)

