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
from stdafx import*

##global matrix 4x4
m4x4 = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0]

#   What a 4x4 matrix math looks like
#   Got a migrane from writing this out
#
#   ---------------     ----------------
#   aX1 aX2 aX3 aX4     bX1 bX2 bX3 bX4
#   aY1 aY2 aY3 aY4  x  bY1 bY2 bY3 bY4
#   aZ1 aZ2 aZ3 aZ4     bZ1 bZ2 bZ3 bZ4
#   aW1 aW2 aW3 aW4     bW1 bW2 bW3 bW4
#   ---------------     ---------------
#
#   aX1 * bX1 + aX2 * bY1 + aX3 * bZ1 + aX4 * bW1, aX1 * bX2 + aX2 * bY2 + aX3 * bZ2 + aX4 * bW2, aX1 * bX3 + aX2 * bY3 + aX3 * bZ3 + aX4 * bW3, aX1 * bX4 + aX2 * bY4 + aX3 * bZ4 + aX4 * bW4
#   aY1 * bX1 + aY2 * bY1 + aY3 * bZ1 + aY4 * bW1, aY1 * bX2 + aY2 * bY2 + aY3 * bZ2 + aY4 * bW2, aY1 * bX3 + aY2 * bY3 + aY3 * bZ3 + aY4 * bW3, aY1 * bX4 + aY2 * bY4 + aY3 * bZ4 + aY4 * bW4
#   aZ1 * bX1 + aZ2 * bY1 + aZ3 * bZ1 + aZ4 * bW1, aZ1 * bX2 + aZ2 * bY2 + aZ3 * bZ2 + aZ4 * bW2, aZ1 * bX3 + aZ2 * bY3 + aZ3 * bZ3 + aZ4 * bW3, aZ1 * bX4 + aZ2 * bY4 + aZ3 * bZ4 + aZ4 * bW4
#   
#   math aint complete, and i aint completing it, this is awful lol...
#
#
#
#
#

"""
    Matrix needed for XY, XZ and YZ grid views and obviously the 3D world
"""

class EulerOrderType:
    MATRIX_TRANSLATE = float
    MATRIX_SCALE = float
    MATRIX_ROTATE = float

def qesPushMatrix()->float:
    return m4x4[0]*m4x4[1]*m4x4[2] == PLANE_X and m4x4[4]*m4x4[5]*m4x4[6] == PLANE_Y and m4x4[8]*m4x4[9]*m4x4[10] == PLANE_Z



m_pEuler = EulerOrderType()



"""
    Some euler functions handlers
"""

#get translation
def sceneGetTranslation()->float:
    return m_pEuler.MATRIX_TRANSLATE

#get scale
def sceneGetScale()->float:
    return m_pEuler.MATRIX_SCALE

#get rotation
def sceneGetRotation()->float:
    return m_pEuler.MATRIX_ROTATE