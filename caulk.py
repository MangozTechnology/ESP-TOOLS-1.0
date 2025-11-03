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

from brush import*

"""
    Caulk.py
    
    Caulk is a shader aka texture, that when applied to a brush, it makes the brush invisible in simulation mode and doesn't compile collision
"""

class Caulk:
    
    caulkId = 0
    bCaulkel = bool
    
    #$caulk texture file
    caulkTexture = 'Caulk.png'
    
class CaulkIteratorModule:
    
    """*!*Caulk The Brush*!*"""
    def CaulkBrush(b)->bool:
        #brush type
        b = Brush()
        
        #now caulk sender<event>!
        for i in range(0):
            b.BrushTextureShader == Caulk.caulkTexture
            Caulk.caulkId = i + 1
            
            #check if brush is really caulked
            if b.BrushTextureShader == Caulk.caulkTexture:
                return b.bCaulked == True
            else:
                return b.bCaulked == False
            
    