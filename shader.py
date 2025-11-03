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

class Texdef:
    texcoords = [0.0, 0.0, 0.0, 0.0]
    bScale = bool
    shadername = str
    
    def getShader(_shader)->str:
        return _shader
    
    def getCoords(_coords)->float:
        return _coords
    
    def getScaleMode(_scalemode)->bool:
        return _scalemode == True
    