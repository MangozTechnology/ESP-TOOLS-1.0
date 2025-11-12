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

import stdafx as xy_t

from brush import*
from qesmatictypes import*
from caulk import*

rectangle = tk.Canvas

class XYWnd(rectangle):
    
    xCur = int
    yCur = int
    
    xPos = 0.0, 0.0, 0.0
    yPos = 0.0, 0.0, 0.0
    
    mColumns = int
    mRows = int
    
    mWidth = int
    mHeight = int
    
    bDragged = bool
    
    #bad code will fix eventually
    mXYMatrix = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0 ,0.0]
    
    xyvec3_t = 0.0, 0.0, 0.0
    viewtype = float
    
    xy_plane = xy_t.p.Plane()
    xy_face = xy_t.f.Face()
    xy_brush = xy_t.primit.Brush()
    
    """"
    def BrushDrawXY(xy_brush):
        #draw brush rect reference as top view
        rectangle.create_polygon(xy_brush.BrushFace, xy_brush.BrushEdges, 0, 0, 0, 0, activedash=0, activefill= '', activewidth= 1, outline= 'red')
    """
        
    """
        *!When mouse click drag in xyview, it creates a new brush!*    
    """
    def NewBrush_Drag():
        any()
        
    def DrawESPXY():
        any()
        
    def DragXYDir_OnMouse():
        any()
        
    def XYZoomIn():
        any()
        
    def XYZoomOut():
        any()
        
    def XYSetWnd(Window):
        set.add(Window)
        
def BrushDrawXY(xy_brush, window):
    #draw brush rect reference as top view
    window.create_polygon(xy_brush.BrushFace, xy_brush.BrushEdges, 10, 100, 400, 800, activefill= '', outline= 'red', width= 2)
        