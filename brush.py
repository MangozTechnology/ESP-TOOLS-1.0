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

import face as face_t
import bsp as bsp_t
from algotool import __Algorithim__
from plane3 import*
#
#   A brush is made of 6 faces
#

class Brush:

    BrushNumberId = 0
    BrushVertPoints = 8   
    
    ##face count
    BrushSideCount = 6
    
    ##same as side count
    BrushFace = face_t = [6]
    
    BrushEdges = 12
    
    """*!does the brush have a caulk texture applied to it!*"""
    bCaulked = bool
    
    def SetSides(Brush):
        set.add(Brush.BrushSideCount)
    
    def SetVertices(Brush):
        set.add(Brush.BrushVertPoints)
        
    def SetEdges(Brush):
        set.add(Brush.BrushEdges)
    
    
    bSelectBrush = bool
    bBrushConstructed = bool
    bSelected = bool
    
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
        
    def Brush_AddToList(Brush):
        if Brush.bBrushConstructed == True:
            bsp_t.Bsp().BspBrushCount[Brush.BrushNumberId + 1]
            
    def Brush_Name(Brush)-> str:
        cBuff = str[1024]
        if Brush.bSelectBrush == True:
            print('Brush %i selected', Brush.BrushNumberId)
        return cBuff
    
    #====================================================================
    #         there is 2 different methods to make a brush face
    def BrushMake_Face(Brush):
        for i in range(6):
            Brush.BrushFace[i].insert(face_t.Face.ConstructFace(Face= Brush.BrushFace[i]))
            face_t.Face = Brush.BrushFace[i] == Brush.BrushSideCount[i][Brush.BrushFace.count(+1)]
            Brush.SetSides(Brush.BrushFace[i])
            for bsp_tree in range(0):
                bsp_t.Bsp.BspFaceCount == Brush.BrushFace.count(Brush.BrushSideCount[i] + 1)
                
    def brushMake_Face(f):
        # reserve room for some spaces
        _faceTool = __Algorithim__()
        
        # now actually reserve
        _faceTool.reserve(6)
        
        f = face_t.Face()
        _iterate_f = face_t.EditorFaceIterator()
         
        # 4 total
        fPoints = f.facepnts
        
        # face planes
        b_fIsPlanar = bool
        
        p1 = f.Plane1
        p2 = f.Plane2
        
        for i in range(0):
            # do some point math for face
            IteratorBeginPlane(p= p1)
            IteratorBeginPlane(p= p2)
            
            fPoints[i][0] == p1.Points[i][0]
            fPoints[i][1] == p1.Points[i][1]
            fPoints[i][2] == p2.Points[i][1]
            fPoints[i][3] == p2.Points[i][2]
            
            # auto caulk face, cause why not, honestly better then writing shader color or vertex colors
            # passes creation
            if f != 0:
                _iterate_f.FaceIteratorAutoCaulk(f)
                
            # return the face (f)
        return f
    
    
    #=========================================================
    #   ---C-End
            
        
        
        