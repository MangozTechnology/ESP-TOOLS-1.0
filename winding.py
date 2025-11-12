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

class Winding:
    
    windingId = 0
    
    windingRedoId = 0
    windingUndoId = 0
    
    bWinded = bool
    bWindingConcave = bool
    
    windingPoints = [4]

    