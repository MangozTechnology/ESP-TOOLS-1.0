
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

"""
==========================================================================
This file loads and holds preferences for the Clip_Robot shader or texture
==========================================================================
"""

class TexTool:
        
    #returns the name, a set of string just an FYI
    def TexToolGetTextureName()-> str:
        return "Clip_Robot.png"
    
    #direct texture call by file
    Texture = 'Clip_Robot.png'