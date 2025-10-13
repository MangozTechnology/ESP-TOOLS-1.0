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

####################################
#                                  #
#   Brush is a 3d geometry shape   #
#                                  #
####################################

import face as f

#
#   A brush is made of 6 faces
#

class Brush:

    
    BrushVertPoints = 8   
    
    ##face count
    BrushSideCount = 6
    
    BrushEdges = 12
    
    def SetSides(Brush):
        set().add(Brush.BrushSideCount)
    
    def SetVertices(Brush):
        set().add(Brush.BrushVertPoints)
        
    def SetEdges(Brush):
        set().add(Brush.BrushEdges)
    
    
    bSelectBrush = bool

    ##brushvectors = f.p.v.vec3_f   | trash variable

    bScalable = bool
    
    BrushTextureShader = str
    
    def SetBrushTexture(Brush) -> str:
        return Brush.BrushTextureShader
    
    def GlobalObserver_BrushScaleMode(Brush) -> bool :
        if True:
            print("----Brush Is In Scale Mode----")
        return Brush.bScalable == True

        def ConstructBrush():
            any()
