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

import mathvec as v

va = v.vec3_f
vb = v.vec3_f
vc = v.vec3_f

class Plane():

    #usally 0.5
    distance = float
    invert = bool

    flip = invert

    points = [0, 0, 0]

    vec_a = v.vec3_f
    vec_b = v.vec3_f
    vec_c = v.vec3_f

    normal = v.vec3_f

    fTextureScale = float


