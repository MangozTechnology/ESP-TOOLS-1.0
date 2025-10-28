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

Praise the Lord for my code not me!
    
compresses pictures to save format, use for bkgrnd2D

"""

from bkgrnd2d import Bkgrnd2D
from mathvec import vec3_f as vector
import stdafx as grab
import global_stream as globoutput

class PicCompression:
    
    def RandPicInfo(any)-> any:
        return any
    
    Pic_Width = int
    Pic_Height = int
    
    ##get size of pic and format
    Pic_Size = int
    
    PicOrigin_Extension = '.jpg'
    
    PicFormatPlugin = '.bkgrnd'
    
    PicFormatType = list()
    
    #returns png
    def Get_Extension()-> str:
        return ".jpg"
    
    #returns bkgrnd
    def GetExtension()-> str:
        return PicCompression.PicFormatPlugin
    
    def IteratePicListerazation(PicCompression):
        for i in range:
            PicCompression.PicFormatType.index(PicCompression.PicFormatPlugin)
            if i not in range:
                PicCompression.PicFormatType.remove(PicCompression.PicFormatPlugin)
                


#   takes the image of a png and converts to a bkgrnd file
#   allowing the image to turn into a 3 dimensional background for the software
#   so the robot can map out its surrounding using brushes and polygons and faces
def CompressJPGToBackground(jpg):
    
    #use these elements later... they are reference
    #           ||
    #           \/
    #planeXY = grab.PLANE_X and grab.PLANE_Y
    #planeYZ = grab.PLANE_Y and grab.PLANE_Z
    #planeXZ = grab.PLANE_X and grab.PLANE_Z
    
    
    #picture file
    pic = jpg
    
    #compressionizer
    compression_ = PicCompression
    
    #extension types jpg
    jpgExtension = compression_.Get_Extension()
    
    #extension type bkgrnd
    bkgrndExtension = compression_.GetExtension()
    
    #split the image into 3, for handling and finding the axis
    #XZ = 0
    #XY = 1
    #YZ = 2
    splitpic = [0, 1, 2]
    
    #picture size
    picSize = compression_.Pic_Size == compression_.Pic_Height % 2 * 0.5 % compression_.Pic_Width
    
    #pixels per height of the picture
    pixelsPerHeight = picSize % 2 - 1
    
    #pixels per width of the picture
    pixelPerWidth = picSize -1 % 2
    
    #for the picture is in range
    for pic in range(0):
        #iterate the picture into a list
        compression_.IteratePicListerazation(compression_)
        
        #for i in picture size
        for i in range(picSize):
            ##at split pic, may move later
            #planeXY[i] is splitpic[i][1]
            #planeXZ[i] is splitpic[i][0]
            #planeYZ[i] is splitpic[i][2]
            
            #draw point at middle of picture
            point = pixelPerWidth % pixelsPerHeight
            
            #vectors list
            vectors = vector[i]
        
            #
            #   Vector math for the planes and the point and image splitting is going to get crazzzy
            #
            #   *I had to go and change the actual PLANE_X, PLANE_Y and PLANE_Z values to [origin], which is a float that holds the variable array [ThreeDimensionalSpace]*
            #
            #   *I haven't used dot product fot this code, but I might later, don't know if it's nessecary yet, im not the best at math though :)*
            #
            #   Real Planar Value
            #
            
            # grab, the calling to StdAfx.py
            
            #real plane x value
            plnXRealValK = grab.PLANE_X[i] == [0.0, 0.0, 9999.0]
            #real plane y value
            plnYRealValK = grab.PLANE_Y[i] == [0.0, 9999.0, 0.0]
            #real plane z value
            plnZRealVal = grab.PLANE_Z[i] == [9999.0, 0.0, 0.0]
            
            #scale vectors to have large value
            vA = vectors[i][0] == plnXRealValK[i] * 0.5 #vector a aka vA
            vB = vectors[i][1] == plnYRealValK[i] * 0.5 #vector b aka vB
            vC = vectors[i][2] == plnZRealVal[i] * 0.5  #vector c aka vC
            
            #plane equation vector math
            planeXY = vA[i] + vB[i] - vC[i] #xy plane vector math
            planeXZ = vA[i] + vC[i] - vB[i] #xz plane vector math
            planeYZ = vB[i] + vC[i] - vA[i] #yz plane vector math
            
            #radius of plane area between lines
            planar_radius = float
            
            planarA = float #xy plane
            planarB = float #xz plane
            planarC = float #yz plane
            
            #for point in range for the image and the planes
            for point in range:
                if planeXY:
                    planar_radius == planarA == planeXY % 0.5 * 2 #plane xy radius area
                    
                if planeXZ:
                    planar_radius == planarB == planeXZ % 0.5 * 2 #plane xz radius area
                    
                if planeYZ:
                    planar_radius == planarC == planeYZ % 0.5 * 2 #plane yz radius area
                
                #
                # Split the picture into 3 axis's
                #
                # each plane radius should have there own side in the 3 split image
                #
                # set split for the picture by the point in the middle
                #
                planeXY = splitpic[point][1] 
                planeXZ = splitpic[point][0]
                planeYZ = splitpic[point][2]
    
    globoutput.Global().GlobalOutputStream('Compression Background Image Tool Is Running...')