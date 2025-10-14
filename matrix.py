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

from mathvec import vec3_f as vec3_t

##global matrix 4x4
m4x4 = vec3_t = [16]

x = float
y = float
z = float

def MatrixIdentity()-> float:
    for i in range(16):
        x[i] = m4x4[i][0], m4x4[i][1], m4x4[i][2], m4x4[i][3]
        y[i] = m4x4[i][4], m4x4[i][5], m4x4[i][6], m4x4[i][7]
        z[i] = m4x4[i][8], m4x4[i][9], m4x4[i][10], m4x4[i][11]
    return x, y, z


    
