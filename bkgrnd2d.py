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

import tkinter as tk
from mathvec import vec3_f as vec_t
import directory as fileBuff
import tkinter.filedialog as filepage

class Bkgrnd2D:

    bkgrndAlongX = vec_t
    bkgrndAlongY = vec_t
    bkgrndAlongZ = vec_t

    #not subscriptable ?? dunno why my arrays suck, im a C++ programmer writing this so... yeah :)
   ## bkgrndBuff = str[2048]
    
    def PointInBkgrndSpace(Bkgrnd2D) -> float:
        return Bkgrnd2D.bkgrndAlongX + Bkgrnd2D.bkgrndAlongY + Bkgrnd2D.bkgrndAlongZ
    
    bkgrndDepth = vec_t
    
    bkgrndPic = str
    bkgrndPicName = str
    
    def ReturnBkgrndPic(Bkgrnd2D)-> str:
        return Bkgrnd2D.bkgrndPic
    
    def OpenBkgrndPic(Bkgrnd2D):
        cBuff = str[1024]
        open(Bkgrnd2D.bkgrndPic, '+a', buffering= cBuff)
        
    def SaveBkgrndPic(Bkgrnd2D):
        any()
        ##save(filename= Bkgrnd2D.bkgrndPicName , ignore_discard=False, ignore_expires=False)

        
    def GetBkgrndFile(Bkgrnd2D) -> str:
        return Bkgrnd2D.bkgrndPicName
    
    def FWriteBkgrndStream(Bkgrnd2D):
        for i in range(Bkgrnd2D.bkgrndPic in fileBuff.__file__ == Bkgrnd2D.bkgrndPicName):
            print('Background X Axis Scale : %f', Bkgrnd2D.bkgrndAlongX[i])
            print('Background Y Axis Scale : %f', Bkgrnd2D.bkgrndAlongY[i])
            print('Background Z Axis Scale : %f', Bkgrnd2D.bkgrndAlongZ[i])
            print('Background Depth Scale : %f', Bkgrnd2D.bkgrndDepth[i])
            
            
class BkgrndPage:
    
    def PaintNewPage():
        page = tk.Tk()
        page.configure(width= 450, height= 350, background= 'Gray26')
        page.title('New Background File')
        
        dirlist = tk.Listbox(page, width= 75, height= 350, relief= 'solid', background= 'Gray26')
        dirlist.pack(side= 'left')
        
        _pageFileDirectory = r"C:Downloads\ESMatic\backgrounds"
        
        _pageFileModule = filepage.Open()
        _pageFileModule.show()
        
        page.mainloop()