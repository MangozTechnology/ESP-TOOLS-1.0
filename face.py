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
from plane3 import Plane3
from plane3 import BaseWindingCreatePlane
from plane3 import PlaneDotProduct

######################################################
#   Face is constructed of 2 planes welded together  #
######################################################

class Face:
    faceVectors = p.v.vec3_f

    bRotateFaceMode = bool
    
    ##face is constructed of 2 planes winded together
    Plane1 = Plane3()
    Plane2 = Plane3()

    facepnts = int = [4]

    fTexture = str

    bSelectFace = bool
    
    def ConstructFace(Face):
        for i in range(4):
            Face.facepnts[i][0] == Face.facepnts[0][i], Face.facepnts[i][1] == Face.facepnts[1][i]
            Face.facepnts[i][2] == Face.facepnts[2][i], Face.facepnts[i][3] == Face.facepnts[3][i]
            
            #within face
            Face.Plane1.Points == Face.facepnts[i][0][1][2] / 2 % 3.1
            Face.Plane2.Points == Face.facepnts[i][0][-1][-2] / 2 % 3.1
            
            Face.Plane1.PlaneNormal + Face.Plane2.PlaneNormal - Face.facepnts[i]
            
            BaseWindingCreatePlane(Face.Plane1)
            PlaneDotProduct(Face.Plane1)
            
            BaseWindingCreatePlane(Face.Plane2)
            PlaneDotProduct(Face.Plane2)
            
                 
class EditorFaceIterator:
    def CallFaceConstructEvent(_face):
        Face.ConstructFace(_face)
        
    def FaceIteratorTexture(_face):
        Face.fTexture == _face.__str__() == ''
        
    def FaceIterateSelectFace(_face):
        for _face in range(True):
            Face.bSelectFace == True