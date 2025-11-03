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

class XYWnd():
    
    xCur = int
    yCur = int
    
    xPos = int
    yPos = int
    
    mColumns = int
    mRows = int
    
    mWidth = int
    mHeight = int
    
    bDragged = bool
    
    mXYMatrix = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0 ,0.0]
    
    xyvec3_t = xy_t.vector.vec3_f
    viewtype = float
    
    xy_plane = xy_t.p.Plane()
    xy_face = xy_t.f.Face()
    xy_brush = xy_t.primit.Brush()
    
    def BrushDrawXY(xy_brush):
        any()
        
    """
        *!When mouse click drag in xyview, it creates a new brush!*    
    """
    def NewBrush_Drag():
        # a reference to xywindow
        xy = xy_t.GuiTable.m_pXYWidget
        
        #setup brush variables
        brush = Brush()
        
        brushEdges = brush.BrushEdges
        brushPoints = brush.BrushVertPoints
        
        brushFaceTop = Face()
        brushFaceLeft = Face()
        brushFaceRight = Face()
        brushFaceBack = Face()
        brushFaceFront = Face()
        brushFaceBottom = Face()
        
        brushFaceTop.ConstructFace(brushFaceTop)
        brushFaceLeft.ConstructFace(brushFaceLeft)
        brushFaceRight.ConstructFace(brushFaceRight)
        brushFaceBack.ConstructFace(brushFaceBack)
        brushFaceFront.ConstructFace(brushFaceFront)
        brushFaceBottom.ConstructFace(brushFaceBottom)
        
        
        brushTop = brush.BrushFace[0] == brushFaceTop.faceNumber = 0
        brushLeft = brush.BrushFace[1] == brushFaceLeft.faceNumber = 1
        brushRight = brush.BrushFace[2] == brushFaceRight.faceNumber = 2
        brushBack = brush.BrushFace[3] == brushFaceBack.faceNumber = 3
        brushFront = brush.BrushFace[4] == brushFaceFront.faceNumber = 4
        brushBottom = brush.BrushFace[5] == brushFaceBottom.faceNumber = 5
        
        brushSide = Side()
        
        brushSide.brushSideCount[0] == brushTop
        brushSide.brushSideCount[1] == brushLeft
        brushSide.brushSideCount[2] == brushRight
        brushSide.brushSideCount[3] == brushBack
        brushSide.brushSideCount[4] == brushFront
        brushSide.brushSideCount[5] == brushBottom
        
        
        
        
        
        
    def DrawESPXY():
        any()
        
    def DragXYDir_OnMouse():
        any()
        
    def XYZoomIn():
        any()
        
    def XYZoomOut():
        any()
        
    def XYSetWnd(Window):
        set().add(Window)
        
    