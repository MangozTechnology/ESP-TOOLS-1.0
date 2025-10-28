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

import stdafx as yz_t

class YZWnd():
    
    xCur = int
    yCur = int
    
    xPos = int
    yPos = int
    
    mColumns = int
    mRows = int
    
    mWidth = int
    mHeight = int
    
    bDragged = bool
    
    mYZMatrix = float
    
    yzvec3_t = yz_t.vector.vec3_f
    viewtype = float
    
    yz_plane = yz_t.p.Plane()
    yz_face = yz_t.f.Face()
    yz_brush = yz_t.primit.Brush()
    
    def BrushDrawYZ(yz_brush):
        any()
        
    def NewBrush_Drag():
        any()
        
    def DrawESPYZ():
        any()
        
    def DragYZDir_OnMouse():
        any()
        
    def YZZoomIn():
        any()
        
    def YZZoomOut():
        any()
        
    def YZSetWnd(Window):
        set().add(Window)