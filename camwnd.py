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
from bkgrnd2d import Bkgrnd2D
from global_stream import*


"""
 functions for the camera window
"""

class CamWnd():
    #weather the 3D camera viewport is frozen, may happen if a brush drawing fails or planes dont wind together properly
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
    def QueBrushDraw(_brush):
        #in range of the camera view
        for i in range(CamWnd):
            grkBegin(_brush)
            GuiTable.m_pCamWidget.create_polygon(_brush)
            grkEnd(_brush)
            
    def CameraReturnMatrix()-> any:
        any()
    
    #no, not color, but a bkgrnd file
    def QueLoadBackground(Bkgrnd2D):
        Bkgrnd2D.Bkrgrnd_File.OpenBkgrndPic()
        
        
        """
        Brush Construction Zone :
            When this is enabled, lines will pertrude outward on all axis's, X, Y and Z, to show were construction zone is
        """
    def BrushConstructionZone():
        #create a reference to the camera window
        viewport = GuiTable.m_pCamWidget
        
        #now draw the lines to show construction zone where brushes can be rendered or scene and created
        #the Y construction line
        viewport.create_line(300, 500, 300, 0, fill= 'red', width= 1, dash= 2)
        #the X construction line
        viewport.create_line(100, 300, 500, 100, fill= 'red', width= 1, dash= 2)
        #the Z construction line
        viewport.create_line(-80, 80, 800, 353, fill= 'red', width= 1, dash= 2)
    
        #message if lines create and dont fail
        Global.GlobalOutputStream('XYZ Construction Zone Line Tool Created...')
        
        #the code for this is actually really simple, it is just the math that is difficult to figure out, but praise to the Lord I figured it out
        #also was going to use stipple's for the line, but for some reason, couldn't create more than one line if I used stipple, so just use dashes

