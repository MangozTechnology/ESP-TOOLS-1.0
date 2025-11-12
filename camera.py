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

class Camera:
    
    cameraIcon = ''
    cameraBuffer = 2048
    
    cameraXProjection = 0.0, 0.0, 0.0
    cameraYProjection = 0.0, 0.0, 0.0
    cameraZProjection = 0.0, 0.0, 0.0
    
    position = 0.0, 0.0, 0.0
    
    orientation = float
    
    fieldOfView = 45.0
    depthView = 100.0
    
    
    def MouseCameraWheelZoomIn():
        return
    
    def MouseCameraWheelZoomOut():
        return
    
    def MouseCameraLeftButton():
        return
    
    def MouseCameraRightButton():
        return
    
    def MouseCameraLeftDownButton():
        return
    
    def MouseCameraRightUpButton():
        return
    
    def DrawPlanes():
        any
    def DrawFaces():
        any
    def DrawBrushes():
        any
        
    def Sender(_func):
        _func
        
    # *!-dimensions-!*
    X = int
    Y = int
    W = int
    H = int
    
    origin = 0.0, 0.0, 0.0
    
    bFreeze = bool
    
    mouse_movposition = 0.0, 0.0, 0.0