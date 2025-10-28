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

import stdafx as xz_t

class XZWnd():
    
    xCur = int
    yCur = int
    
    xPos = int
    yPos = int
    
    mColumns = int
    mRows = int
    
    mWidth = int
    mHeight = int
    
    bDragged = bool
    
    mXZMatrix = float
    
    xzvec3_t = xz_t.vector.vec3_f
    viewtype = float
    
    xz_plane = xz_t.p.Plane()
    xz_face = xz_t.f.Face()
    xz_brush = xz_t.primit.Brush()
    
    def BrushDrawXZ(xz_brush):
        any()
        
    def NewBrush_Drag():
        any()
        
    def DrawESPXZ():
        any()
        
    def DragXZDir_OnMouse():
        any()
        
    def XZZoomIn():
        any()
        
    def XZZoomOut():
        any()
        
    def XZSetWnd(Window):
        set().add(Window)