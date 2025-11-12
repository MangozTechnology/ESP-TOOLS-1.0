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
from qesmatictypes import*
from map import Map as world
from tkinter import messagebox as caulkDlg

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
            

        """
            Caulk The Selected Brush
        """
    def CaulkSelectedBrush():            
        caulkSelBrush = CaulkIteratorModule()
        selBrush = Brush()#the selected brush
    
        if selBrush.bSelected == True:
        #here is the tricky part since this is true, we have to search thye map and find the selected brush, since this function goes into a menu we cant have any variables in the constructor-
        #for this function, so it doesn't automatically execute
        
        #create a reference to the global brush table, so we can get brush, this makes it less tricky
            m_brshTable = QES_GlobalBrushTable()
        
            m_brshTable.PFN_GET_BRUSH(world.brushes == selBrush) # get the brush by using Map.brushes which is equal to selBrush so it finds the brush thats select in the world
            selBrush.BrushNumberId == world.brushes.BrushNumberId.bit_count() # get the absolute brush number id in the world
        #now caulk the brush
            caulkSelBrush.CaulkBrush(selBrush)
            
        else:
        #if this is false the create a dialog message to tell the user no brush is selected
                caulkDialog = caulkDlg.showerror('Caulk Error', message= 'No brush selected to caulk. Make sure a brush is selected.', icon= 'error')
        