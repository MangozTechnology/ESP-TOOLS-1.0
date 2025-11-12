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

import aabb as box
import bkgrnd2d as bkgrnd
import brush as primit
import directory as path
import face as f
import gridfunc as grid
import grklib as glib
import mathvec as vector
import node as entity
import plane as p
import point as pnt
import texturedirectory as textool
import viewport as mapview
import tkinter as tk
from tkinter import dialog as dlg
from tkinter import messagebox as MSGBOX
import texturewnd as texwnd

#================================
#           Gui Table
class GuiTable():
    MainWindow = tk.Tk()
    
    m_pXYWidget = tk.Canvas(MainWindow, relief= 'sunken', background= 'Snow', bd = 3, width= 730, height= 400, scrollregion=(0, 0, 1000, 1000))
    m_pXZWidget = tk.Canvas(MainWindow, relief= 'sunken', background= 'Snow', bd = 3, width= 730, height= 400)
    m_pYZWidget = tk.Canvas(MainWindow, relief= 'sunken', background= 'Snow', bd = 3, width= 800, height = 400)
    m_pCamWidget = tk.Canvas(MainWindow, relief= 'sunken', bg= 'DarkGray', bd= 3, width= 800, height= 400)

#====================================
#
#         XY Window Stuff
#
#====================================

#--------Note : Discard
##def AddXZ():
##   GuiTable.m_pXZWidget.pack(side= 'left', anchor= 'sw')

m_pGridDummy = GuiTable.m_pXYWidget

#====================================
#Draw The Grid
w = int
h = int
ratio = int
def PaintXYGrid(m_pGridDummy, w, h, ratio):
    #vertical lines
    for x in range(0, w, ratio):
        m_pGridDummy.create_line(x, 0, x, h, fill= 'Gray')

    #horizontal lines
    for y in range(0, h, ratio):
        m_pGridDummy.create_line(0, y, w, y, fill= 'Gray')    
    
    print('---Grid Drawing Not Queded, Grid Draw()---')
    
def PrintGridViewType(m_pGridDummy):
    if m_pGridDummy == GuiTable.m_pXYWidget:
        m_pGridDummy.create_text(25, 25, text= "|__", font= ("Consolas", 15), fill = "blue")
    if m_pGridDummy == GuiTable.m_pXZWidget:
        m_pGridDummy.create_text(25, 25, text= "/__", font= ("Consolas", 15), fill = "blue")
    if m_pGridDummy == GuiTable.m_pYZWidget:
        m_pGridDummy.create_text(25, 25, text= "|/", font= ("Consolas", 15), fill = "blue")

#moved to brush.py
"""
def SelectBrush(dummy_brush):
    for primit.f in range( primit.Brush(dummy_brush) ):
        primit.Brush(dummy_brush).frontface.bSelectFace == True
        primit.Brush(dummy_brush).backface.bSelectFace == True
        primit.Brush(dummy_brush).bottomface.bSelectFace == True
        primit.Brush(dummy_brush).leftface.bSelectFace == True
        primit.Brush(dummy_brush).rightface.bSelectFace == True
        primit.Brush(dummy_brush).topface.bSelectFace == True

        primit.Brush(dummy_brush).bScalable == True

        continue

    return dummy_brush
"""


vec = vector.vec3_f

###points = primit.Brush().pnts

shader = textool.g_pClipShader

#
#   Create A New Brush
#
"""
def CreateBrush(vec, f1, f2, f3, f4, f5, f6, shader, points, bSelect = bool):
    brushVolume = box.AABB()
    brush = primit.Brush()
    
    #reserve for faces
    reserve(6)
       
    for i in range(0):

        brushVolume.BoxPoints == points
        vol = brushVolume.BoxVectors[8] = { 0.0 * 2 / 0.5, 1.0 * 2 / 0.5, 2.0 * 2 / 0.5, 3.0 * 2 / 0.5, 4.0 * 2 / 0.5, 5.0 * 2 / 0.5, 6.0 * 2 / 0.5, 7.0 * 2 / 0.5 }
        brushVolume.Height = vol / 0.5
        brushVolume.Width = vol / 1.5
        
        for brushVolume in range(points):
            brush.topface = f1 = vol[0]
            brush.leftface = f2 = vol[1]
            brush.frontface = f3 = vol[2]
            brush.rightface = f4 = vol[3]
            brush.rightface = f5 = vol[4]
            brush.bottomface = f6 = vol[5]

            if bSelect == True:
                SelectBrush(brush)
                HighlightBrush(brush)
        brush.brushtexture = shader

        
def ScaleBrush(dummy_brush):
    brush = primit.Brush(dummy_brush)
    if SelectBrush(brush) and brush.bScalable == True:
        if MB_LEFTDRAG and brush in range(True):
            brush.frontface.faceVectors * 2 / 0.5
            brush.bottomface.faceVectors * 2 / 0.5
            brush.leftface.faceVectors * 2 / 0.5
            brush.rightface.faceVectors * 2 / 0.5
            brush.backface.faceVectors * 2 / 0.5
            brush.topface.faceVectors * 2 / 0.5
"""
            
def CreateSplashScreen():
    pSplash = tk.Tk()
    pSplash.title('Splash Screen')
    
    pPanel = tk.PanedWindow(pSplash, relief= 'sunken', width= 2000, height= 2000, bg= 'White', bd= 1.5)
    pPanel.pack_configure(fill= 'both', expand= True)

def CreateCubePreferencesDlg():
    pWindow = tk.Tk()
    pWindow.title('Cube Preferences')
    pWindow.config(width= 500, height= 300)
    
    pFrame = tk.PanedWindow(pWindow, width= 500 / 1.5, height= 500 / 1.5, relief= 'ridge', bg= 'White')
    pFrame.pack_configure(side='left', anchor= 'n')
    
    bMaxFaceLabel= tk.Label(pFrame, text= 'Brush Max Face Count :')
    bMaxFaceLabel.pack()
    
    bMaxInput = tk.Text(pFrame, relief= 'sunken', width= 15, height= 1, bg= 'White')
    bMaxInput.pack()
    
#=========================
#   Math Section

#====================
#this code should be done in the matrix.py file but this was started first
XYZ = vector.vec3_f
ThreeDimensionalSpace = XYZ

#_SpaceRatio = XYZ #divided by a number ?
SIDE_FRONT = 0
SIDE_SEL = 2
SIDE_BK = 1
SIDE_CROSS_PLANE = -1

PI = 3.14159265358979323846

origin = ThreeDimensionalSpace

PLANE_X = origin[2]
PLANE_Y = origin[1]
PLANE_Z = origin[0]

TRUE_EPSILON = 0.001

def CompareVectors(v1, v2) -> bool:
    any()
    
def DotProduct(x, y) -> float:
    return (x)[0] * (y)[0] + (x)[1] * (y)[1] + (x)[2] * (y)[2]
    
def VecSub(x, y, z) -> float:
    (z)[0] = (x)[0] - (y)[0],
    (z)[1] = (x)[1] - (y)[1],
    (z)[2] = (x)[2] - (y)[2] 
    
    
#=========================
#   Camera Window Stuff

RenderMode_Wireframe = int
RenderMode_Full = int
RenderMode_Fake = int

Viewtype = int

def ReturnRenderMode(mode) -> int:
    return mode

def ReturnViewType(viewtype) -> int:
    return viewtype


def InitRender():
   print('---Camera Window Initalized---')
   RenderMsgBox = MSGBOX.askokcancel('Camera Window Construction', 'Camera Window 3D Viewport Initalized', icon= 'info')
   for i in range(0):
       GuiTable.m_pCamWidget.coords(origin)
       GuiTable.m_pCamWidget.canvasx()
       GuiTable.m_pCamWidget.canvasy()
    
    
#========================
#     Script Window       
def CreateScriptWindow():
    Window = tk.Tk()
    Window.title('Script Window')

    #textbox
    ScriptPanel = tk.Text(Window, bg= 'Black', relief= 'sunken', bd= 2, font= 'TkFixedFont', foreground= 'White', height= 2000, cursor= 'xterm', blockcursor= True)
    ScriptPanel.pack(fill= 'both')


    Window.mainloop()

def GridDrawRectangle(m_pGridDummy):
    m_pGridDummy.create_rectangle(10, 10, 300, 300, fill= "", outline="red", width= 2)
    print('---Brush Size :', 300, 300,'---')
    
def DrawAABBVolumeBox():
    CameraWnd = GuiTable.m_pCamWidget
    CameraWnd.create_polygon(300, 300, 300, 100, 300, 300, 100, 500, fill="", outline= 'blue')
    print('---Drawing AABB---')
    
def DrawGlobalsWindow():
    widget = tk.Tk()
    widget.title('World')
    widget.config(width= 450, height= 450)
    
    entlst = tk.Listbox(widget, relief= 'sunken', bg= 'White', bd= 1.5, width= 450, height= 450)
    entlst.pack()
    
    widget.mainloop()
    

    