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

class XYWnd(xy_t.m_pGridDummy):
    
    xCur = int
    yCur = int
    
    xPos = int
    yPos = int
    
    mColumns = int
    mRows = int
    
    mWidth = int
    mHeight = int
    
    bDragged = bool
    
    xyvec3_t = xy_t.vector.vec3_f
    viewtype = xy_t.PLANE_X
    
    xy_plane = xy_t.p.Plane()
    xy_face = xy_t.f.Face()
    xy_brush = xy_t.primit.Brush()
    
    def BrushDrawXY(xy_brush):
        any()
        
    def NewBrush_Drag():
        any()
        
    def DrawESPXY():
        any()