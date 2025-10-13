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

import tkinter as tk
from mathvec import vec3_f as vec_t

class Bkgrnd2D:

    bkgrndAlongX = vec_t
    bkgrndAlongY = vec_t
    bkgrndAlongZ = vec_t
    
    def PointInBkgrndSpace(Bkgrnd2D) -> float:
        return Bkgrnd2D.bkgrndAlongX + Bkgrnd2D.bkgrndAlongY + Bkgrnd2D.bkgrndAlongZ
    
    bkgrndDepth = vec_t
    
    bkgrndPic = str
    
    def ReturnBkgrndPic(Bkgrnd2D)-> str:
        return Bkgrnd2D.bkgrndPic
    
    def OpenBkgrndPic(Bkgrnd2D):
        i = str[64]
        open(Bkgrnd2D.bkgrndPic, '+a', buffering= i)