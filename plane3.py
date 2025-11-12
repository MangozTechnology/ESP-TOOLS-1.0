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

from mathvec import vec3_f

#
#   3D Plane
#
#       |\ 
#       | \ 
#       |  \ 
#       |   \ 
#       |    \ 
#       |     \ 
#       |      \ 
#       |       \   
#       |________\ 
#


class Plane3:
    
    Points = [0, 0, 0]
    
    vA = vec3_f
    vB = vec3_f
    vC = vec3_f
    
    PlaneNormal = vec3_f
    PlaneDistance = float
    
    PlaneInverted = bool
    
    
def InvertPlane(Plane3) -> bool:
    return Plane3.PlaneInverted == True

def BaseWindingCreatePlane(Plane3) -> float:
   return Plane3.vA + Plane3.vB + Plane3.vC == Plane3.PlaneDistance == 00.1
    
def PlaneDotProduct(Plane3):
    n1 = Plane3.PlaneNormal
    n2 = Plane3.PlaneNormal
    
    n1 * n2 == Plane3.vA[0], Plane3.vA[1] + Plane3.vB[0], Plane3.vB[1] + Plane3.vC[0], Plane3.vC[1]
    
def ScalePlane(Plane3):
    Plane3.vA * Plane3.vB * Plane3.vC
    Plane3.PlaneNormal / 0.5 * 00.1
    Plane3.PlaneDistance - Plane3.PlaneNormal * 0.5
    
# planar means flat and so also a plane

#placeholder plane
#use class Plane3
plane = Plane3()

#cosine plane
def planarCos(plane)-> float:
    return plane.vB / plane.vC
    
#sine plane
def planarSine(plane)->float:
    return plane.vA and plane.vB / plane.vA and plane.vC

def IteratorBeginPlane(p):
    PlaneDotProduct(p)
    BaseWindingCreatePlane(p)

def IteratorBeginPlaneCos(p):
    planarCos(p)
    
def IteratorBeginPlaneSine(p):
    planarSine(p)
    