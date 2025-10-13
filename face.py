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

import plane as p

######################################################
#   Face is constructed of 2 planes welded together  #
######################################################

class Face():
    faceVectors = p.v.vec3_f

    facepln1 = p.Plane()
    facepln2 = p.Plane()

    bRotateFaceMode = bool

    facepnts = int = [4]

    fTexture = str

    bSelectFace = bool