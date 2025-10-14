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

from string import string
import brush
import face
import plane3

class Map:
    
    Map_Name = str[64]
    Map_Path = str[2048]
    
    brushes = brush.Brush()
    faces = face.Face()
    planes = plane3.Plane3()
    
    