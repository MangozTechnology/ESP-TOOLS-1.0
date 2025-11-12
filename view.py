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

import tkinter as viewwindow

orthoview = viewwindow.Canvas

class View(orthoview):
    
    def pushViewAxisType(_axis, _axi)->float:
        return _axis