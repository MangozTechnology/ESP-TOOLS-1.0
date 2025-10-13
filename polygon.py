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

import stdafx as std

class Polygon():
    Mins = std.vector.vec3_f[-16]
    Maxs = std.vector.vec3_f[16]
    
    Select = bool