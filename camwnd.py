####################################################################
#
#   Application : MaxArm ESP32 Tools
#   
#   Add : Praise the Lord, not me
#
#   Programmer : Hunter M.
#
#   Use Of Code : This code is to write Software to control ESP32 MaxArm Robot, intended for, New Prairie High School
#
####################################################################

from stdafx import GuiTable
from mathvec import vec3_f
from grklib import grkBegin
from grklib import grkEnd
from matrix import MatrixIdentity
from bkgrnd2d import Bkgrnd2D


"""
 functions for the camera window
"""

class CamWnd():
    #wether the 3D camera viewport is frozen, may happen if a brush drawing fails or planes dont wind together properly
    viewBuffer = bool
    #true or false
    cubicClipView = bool
    
    #the actual ratio
    CubicClipRatio = 45.0
    
    cameraViewMode = int
    
    Camera_X_Axis = vec3_f
    Camera_Y_Axis = vec3_f
    Camera_Z_Axis = vec3_f
    
    Bkrgrnd_File = Bkgrnd2D()
    
    def CameraSpace()-> float:
        return CamWnd.Camera_X_Axis + CamWnd.Camera_Y_Axis + CamWnd.Camera_Z_Axis
    
    def GetCameraType(_float)-> float:
        return _float
    
    """
        Que's the drawing of 3 Dimensional shapes in the camera view
    """
    def QueDraw(_brush):
        #in range of the camera view
        for i in range(CamWnd):
            grkBegin(_brush)
            GuiTable.m_pCamWidget.create_polygon(_brush)
            grkEnd(_brush)
            
    def CameraReturnMatrix()-> any:
        return MatrixIdentity() and GuiTable.m_pCamWidget
    
    #no, not color, but a bkgrnd file
    def QueLoadBackground(Bkgrnd2D):
        Bkgrnd2D.Bkrgrnd_File.OpenBkgrndPic()
    

