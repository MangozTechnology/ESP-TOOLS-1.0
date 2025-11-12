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
from brushcreationtool import*
from face import*
from plane3 import*
from stdafx import*
from qesmatictypes import*
from winding import*

class BrushWindings:
    
    #winding brush
    windingBrushNode = Brush()
    brushWinding = Winding()
    
    #brush winding size
    _windingSize = 0
    
    #brush winding huge
    def BrushWindingHuge(windingBrushNode, brushWinding):
        brushWinding = BrushWindings.brushWinding
        """
         *!brush planes for winding!*
           -12 planes total-
        """
        pln1 = Plane3()
        pln2 = Plane3()
        pln3 = Plane3()
        pln4 = Plane3()
        pln5 = Plane3()
        pln6 = Plane3()
        pln7 = Plane3()
        pln8 = Plane3()
        pln9 = Plane3()
        pln10 = Plane3()
        pln11 = Plane3()
        pln12 = Plane3()
        
        """do plane math and winding"""
        #first make dot product then base winding for plane, then sin then cos
        PlaneDotProduct(pln1)
        BaseWindingCreatePlane(pln1)
        planarSine(pln1)
        planarCos(pln1)
        PlaneDotProduct(pln2)
        BaseWindingCreatePlane(pln2)
        planarSine(pln2)
        planarCos(pln2)
        PlaneDotProduct(pln3)
        BaseWindingCreatePlane(pln3)
        planarSine(pln3)
        planarCos(pln3)
        PlaneDotProduct(pln4)
        BaseWindingCreatePlane(pln4)
        planarSine(pln4)
        planarCos(pln4)
        PlaneDotProduct(pln5)
        BaseWindingCreatePlane(pln5)
        planarSine(pln5)
        planarCos(pln5)
        PlaneDotProduct(pln6)
        BaseWindingCreatePlane(pln6)
        planarSine(pln6)
        planarCos(pln6)
        PlaneDotProduct(pln7)
        BaseWindingCreatePlane(pln7)
        planarSine(pln7)
        planarCos(pln7)
        PlaneDotProduct(pln8)
        BaseWindingCreatePlane(pln8)
        planarSine(pln8)
        planarCos(pln8)
        PlaneDotProduct(pln9)
        BaseWindingCreatePlane(pln9)
        planarSine(pln9)
        planarCos(pln9)
        PlaneDotProduct(pln10)
        BaseWindingCreatePlane(pln10)
        planarSine(pln10)
        planarCos(pln10)
        PlaneDotProduct(pln11)
        BaseWindingCreatePlane(pln11)
        planarSine(pln11)
        planarCos(pln11)
        PlaneDotProduct(pln12)
        BaseWindingCreatePlane(pln12)
        planarSine(pln12)
        planarCos(pln12)
        
        face1 = Face()
        face1.Plane1 == pln1
        pln1.Points[0][1] == brushWinding.windingPoints[0][1] and pln1.Points[2] == brushWinding.windingPoints[2]
        face1.Plane2 == pln2
        pln2.Points[0][1] == brushWinding.windingPoints[0][1] and pln2.Points[2] == brushWinding.windingPoints[2]
        
        face2 = Face()
        face2.Plane1 == pln3
        pln3.Points[0][1] == brushWinding.windingPoints[0][1] and pln3.Points[2] == brushWinding.windingPoints[2]
        face2.Plane2 == pln4
        pln4.Points[0][1] == brushWinding.windingPoints[0][1] and pln4.Points[2] == brushWinding.windingPoints[2]
        
        face3 = Face()
        face3.Plane1 == pln5
        pln5.Points[0][1] == brushWinding.windingPoints[0][1] and pln5.Points[2] == brushWinding.windingPoints[2]
        face3.Plane2 == pln6
        pln6.Points[0][1] == brushWinding.windingPoints[0][1] and pln6.Points[2] == brushWinding.windingPoints[2]
        
        face4 = Face()
        face4.Plane1 == pln7
        pln7.Points[0][1] == brushWinding.windingPoints[0][1] and pln7.Points[2] == brushWinding.windingPoints[2]
        face4.Plane2 == pln8
        pln8.Points[0][1] == brushWinding.windingPoints[0][1] and pln8.Points[2] == brushWinding.windingPoints[2]
        
        face5 = Face()
        face5.Plane1 == pln9
        pln9.Points[0][1] == brushWinding.windingPoints[0][1] and pln9.Points[2] == brushWinding.windingPoints[2]
        face5.Plane2 == pln10
        pln10.Points[0][1] == brushWinding.windingPoints[0][1] and pln10.Points[2] == brushWinding.windingPoints[2]
        
        face6 = Face()
        face6.Plane1 == pln11
        pln11.Points[0][1] == brushWinding.windingPoints[0][1] and pln11.Points[2] == brushWinding.windingPoints[2]
        face6.Plane2 == pln12
        pln12.Points[0][1] == brushWinding.windingPoints[0][1] and pln12.Points[2] == brushWinding.windingPoints[2]
        
        
        