
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
#do sum imports
import stdafx as gp
from tkinter import ttk
from global_stream import Global
from time import time
from xywnd import XYWnd
from xzwnd import XZWnd
from yzwnd import YZWnd
from tkinter import PhotoImage
from bkgrnd2d import BkgrndPage
from simulationwindow import CreateSimulationWindow
from gridfunc import GridDrawQue
from viewport import DrawPlane
from viewport import DrawPolygon
from qesmatictypes import*
from camwnd import*


#g_pSplashScreen = gp.tk.Tk()
#g_pSplashScreen.title('Splash Screen')
#g_pSplashScreen.configure(width= 600, height= 600, background= 'AntiqueWhite')

##g_pSplashImage = gp.tk.PhotoImage(name='SPLASH', master=g_pSplashScreen , format = 'PNG', file = 'app\esp_splash_logo' + '.png')

#g_pSplashCanvas = gp.tk.Canvas(g_pSplashScreen, width= 600, height= 600, relief= 'sunken', bg= 'white', bd = 2)
##g_pSplashCanvas.create_image(800, 300, image= g_pSplashImage)
##g_pSplashCanvas.pack(fill = 'both')

#def CallSplashTick():
    ##if time == 2 == True:
   # g_pSplashScreen.destroy()

##=============================================================================================================     
##call splash tick()-> True, we want to instantly destroy window, not gonna mess with timer variables
##CallSplashTick()

"""
    *!SPLASH SCREEN INSTANTLY DESTROYS, NOT MESSING WITH TIMER, TO MUCH TIME WASTED, CANT GET TICK TIMER SET TO TWO SECONDS!*
"""

g_pMainFrame = gp.GuiTable.MainWindow
g_pMainFrame.title('ESMatic - Version 1.0 ( Fall 2025 )')

#=========================
#   Global Widgets

g_pMenuBar = gp.tk.Menu(g_pMainFrame, type= 'menubar')
g_pFileMenu = gp.tk.Menu(g_pMenuBar)
g_pMenuBar.configure(bg= 'black')
g_pFileMenu.add_command(label= 'New ESP Map')
g_pFileMenu.add_command(label= 'Open ESP Map', command= OpenMapDialog)
g_pFileMenu.add_command(label= 'Save ESP Map')
g_pFileMenu.add_command(label= 'Save ESP Map As...')
g_pFileMenu.add_separator()
g_pFileMenu.add_command(label= 'Exit ESP Map', command= g_pMainFrame.quit)
g_pMenuBar.add_cascade(label= 'File', menu= g_pFileMenu)

g_pEditMenu = gp.tk.Menu(g_pMenuBar)
g_pEditMenu.add_command(label= 'Cube Preferences', command= gp.CreateCubePreferencesDlg)
g_pEditMenu.add_command(label= 'Camera Preferences')
g_pEditMenu.add_separator()
g_pEditMenu.add_command(label= 'Directory Preferences')
g_pMenuBar.add_cascade(label= 'Edit', menu= g_pEditMenu)

g_pMiscMenu = gp.tk.Menu(g_pMenuBar)
g_pMiscMenu.add_command(label= 'Render Options')
g_pMiscMenu.add_separator()
g_pMiscMenu.add_command(label= 'Color Table')
g_pMenuBar.add_cascade(label= 'Misc', menu= g_pMiscMenu)

#praise the Lord for my code, not me

g_pHelpMenu = gp.tk.Menu(g_pMenuBar)
g_pHelpMenu.add_command(label = 'About')
g_pMenuBar.add_cascade(label= 'Help', menu= g_pHelpMenu)

g_pMainFrame.config(menu= g_pMenuBar)

g_pViewMenu = gp.tk.Menu(g_pMenuBar)
g_pViewMenu.add_command(label= 'XY')
g_pViewMenu.add_command(label= 'YZ')
g_pViewMenu.add_command(label= 'XZ')
g_pMenuBar.add_cascade(label='View', menu= g_pViewMenu)

g_pConnectionMenu = gp.tk.Menu(g_pMenuBar)
g_pConnectionMenu.add_command(label= 'Find ESP32 MaxArm')
g_pMenuBar.add_cascade(label= 'Connection', menu = g_pConnectionMenu)

g_pBindingsMenu = gp.tk.Menu(g_pMenuBar)
g_pBindingsMenu.add_command(label= 'MaxArm_Set<>')
g_pBindingsMenu.add_command(label= 'MaxArm_Algorithm<>')
g_pBindingsMenu.add_command(label= 'MaxArm_Tracing<>')
g_pMenuBar.add_cascade(label= 'Bindings', menu= g_pBindingsMenu)

g_pVersionMenu = gp.tk.Menu(g_pMenuBar)
g_pVersionMenu.add_command(label= 'I only made one version!')
g_pMenuBar.add_cascade(label= 'Versions', menu= g_pVersionMenu)

g_pWindowMenu = gp.tk.Menu(g_pMenuBar)
g_pWindowMenu.add_command(label= 'Window->Title() == ? str')
g_pWindowMenu.add_command(label= 'Window->Layout() == ? : TYPE')
g_pWindowMenu.add_separator()
g_pWindowMenu.add_command(label= 'Create Your Own Window', command= gp.CreateScriptWindow)
g_pMenuBar.add_cascade(label= 'Window Handling', menu= g_pWindowMenu)

g_pTextureMenu = gp.tk.Menu(g_pMenuBar)
g_pTextureMenu.add_command(label= 'Shader Window', command= gp.texwnd.DrawTextureWindow)
g_pTextureMenu.add_separator()
g_pTextureMenu.add_command(label= 'Clip Selected Brush')
g_pMenuBar.add_cascade(label= 'Texture', menu= g_pTextureMenu)

g_pClipMenu = gp.tk.Menu(g_pMenuBar)
g_pClipMenu.add_command(label= 'Add Point')
g_pClipMenu.add_command(label= 'Delete Point')
g_pMenuBar.add_cascade(label= 'Clip Point', menu= g_pClipMenu)

g_pMotherboard = gp.tk.Menu(g_pMenuBar)
g_pMotherboard.add_command(label= 'Motherboard Editor')
g_pMenuBar.add_cascade(label= 'Motherboard', menu= g_pMotherboard)

g_pPluginsMenu = gp.tk.Menu(g_pMenuBar)
g_pPluginsMenu.add_command(label= 'Mouse Plugins...')
g_pPluginsMenu.add_command(label= 'Icon Plugins...')
g_pMenuBar.add_cascade(label= 'Plugins', menu= g_pPluginsMenu)

g_pTerminalMenu = gp.tk.Menu(g_pMenuBar)
g_pTerminalMenu.add_command(label= 'Powershell')
g_pTerminalMenu.add_command(label= 'Command Prompt')
g_pTerminalMenu.add_command(label = 'ESP Terminal')
g_pMenuBar.add_cascade(label= 'Terminals', menu= g_pTerminalMenu)

g_pEntityMenu = gp.tk.Menu(g_pMenuBar)
g_pEntityMenu.add_command(label= 'Path Node')
g_pEntityMenu.add_command(label= 'Idle Node')
g_pEntityMenu.add_command(label= 'Target Node')
g_pEntityMenu.add_command(label= 'Kill Node')
g_pEntityMenu.add_separator()
g_pEntityMenu.add_command(label= 'Face')
g_pEntityMenu.add_command(label= 'Brush')
g_pEntityMenu.add_command(label= 'Polygon')
g_pEntityMenu.add_command(label= 'Clip')
g_pEntityMenu.add_command(label= 'Null Robot')
g_pMenuBar.add_cascade(label= 'Entities', menu= g_pEntityMenu)

g_pRenderMenu = gp.tk.Menu(g_pMenuBar)
g_pRenderMenu.add_command(label= 'Lighting Wireframe')
g_pRenderMenu.add_command(label= 'Lighting Full')
g_pRenderMenu.add_command(label= 'Lighting Fake')
g_pRenderMenu.add_separator()
g_pRenderMenu.add_command(label= 'Init 3D Viewport', command= gp.InitRender)
g_pMenuBar.add_cascade(label= 'Render', menu = g_pRenderMenu)

g_pWorldMenu = gp.tk.Menu(g_pMenuBar)
g_pWorldMenu.add_command(label= 'Globals', command= gp.DrawGlobalsWindow)
g_pMenuBar.add_cascade(label= 'World', menu= g_pWorldMenu)

g_pVolumeMenu = gp.tk.Menu(g_pMenuBar)
g_pVolumeMenu.add_command(label= 'New Volume Box', command= gp.DrawAABBVolumeBox)
g_pMenuBar.add_cascade(label= 'Volume', menu= g_pVolumeMenu)

g_pBkgrndMenu = gp.tk.Menu(g_pMenuBar)
g_pBkgrndMenu.add_command(label= 'New Bkgrnd Image', command= BkgrndPage.PaintNewPage)
g_pBkgrndMenu.add_command(label= 'Open Bkgrnd Image')
g_pBkgrndMenu.add_command(label= 'Save Bkgrnd Image')
g_pMenuBar.add_cascade(label= 'Bkgrnd', menu= g_pBkgrndMenu)

g_pXYWnd = gp.GuiTable.m_pXYWidget
g_pXYWnd.grid(row= 0, column= 0)

g_pCamWnd = gp.GuiTable.m_pCamWidget
g_pCamWnd.grid(row=0, column= 1)

g_pXZWnd = gp.GuiTable.m_pXZWidget
g_pXZWnd.grid(row= 1, column= 0)

g_pYZWnd = gp.GuiTable.m_pYZWidget
g_pYZWnd.grid(row= 1, column= 1)

gp.PrintGridViewType(g_pXYWnd)
gp.PrintGridViewType(g_pXZWnd)
gp.PrintGridViewType(g_pYZWnd)

#GridDrawQue.GridDrawBlock(g_pXYWnd)
#GridDrawQue.GridDrawBlock(g_pXZWnd)
#GridDrawQue.GridDrawBlock(g_pYZWnd)

#NewBrush_DragEvent = g_pXYWnd.bind("<Button-1>")

#dummy plane drawing regression test
#DrawPlane(g_pXYWnd)
#DrawPlane(g_pXZWnd)
#DrawPlane(g_pYZWnd)

#DrawPolygon(g_pCamWnd)

def RealRECT_Draw():
        gp.GridDrawRectangle(g_pXYWnd)
        gp.GridDrawRectangle(g_pXZWnd)
        gp.GridDrawRectangle(g_pYZWnd)

g_fGridWidth = 1000
g_fGridHeight = 1000
g_fGridRatio = 35

prev_grd = gp.tk.Canvas()

def CallBackPrevGrid(prev_grd):
    return prev_grd

def XYZoomInScale(g_fGridRatio):
    return g_fGridRatio * 2 + 0.5

def XYZoomPrint():
    print("Grid Zoom()->XY Sucessfull")

def ClearPrevLines():
    del g_fGridRatio
    
"""
---*HAVING SERIOUS GRID ISSUES, ZOOM IS NOT WORKING*---

DEBUG:
    I think I might know the issue, the grid doesn't redraw when I go to zoom so it constantly que's the last grid or the current grid without updating to new window

"""
    
def GridZoomOut8():
    zoomRatio = 8
    
    gp.PaintXYGrid(g_pXYWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    gp.PaintXYGrid(g_pXZWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    gp.PaintXYGrid(g_pYZWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    
    Global.GlobalOutputStream('Grid Size : 8')
        
    
def GridZoomOut32():
    zoomRatio = 24
    
    gp.PaintXYGrid(g_pXYWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    gp.PaintXYGrid(g_pXZWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    gp.PaintXYGrid(g_pYZWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    
    Global.GlobalOutputStream('Grid Size : 32')
    
def GridZoomOut64():
    zoomRatio = 64
    
    gp.PaintXYGrid(g_pXYWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    gp.PaintXYGrid(g_pXZWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    gp.PaintXYGrid(g_pYZWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    
    Global.GlobalOutputStream('Grid Size : 64')
    
def GridZoomOut81():
    zoomRatio = 81
    
    gp.PaintXYGrid(g_pXYWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    gp.PaintXYGrid(g_pXZWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    gp.PaintXYGrid(g_pYZWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    
    Global.GlobalOutputStream('Grid Size : 81')
    
def GridZoomOut128():
    zoomRatio = 128
    
    gp.PaintXYGrid(g_pXYWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    gp.PaintXYGrid(g_pXZWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    gp.PaintXYGrid(g_pYZWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    
    Global.GlobalOutputStream('Grid Size : 128')
    
def GridZoomOut164():
    zoomRatio = 164
    
    gp.PaintXYGrid(g_pXYWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    gp.PaintXYGrid(g_pXZWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    gp.PaintXYGrid(g_pYZWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    
    Global.GlobalOutputStream('Grid Size : 164')
    

#---BAD---
"""
def RedrawWindows():
    
    XY = g_pXYWnd
    YZ = g_pYZWnd
    XZ = g_pXZWnd
    
    del XY
    del XZ
    del YZ
"""

"""

    Another issue : reset grid windows is not working properly either! :(

"""

#def GlobalCommand_Observer_ResetGridWindows():
#    g_pXYWnd.destroy()
#    g_pXZWnd.destroy()
#    g_pYZWnd.destroy()
   
g_pGridMenu = gp.tk.Menu(g_pMenuBar)
g_pGridMenu.add_command(label= 'Grid 8',command= GridZoomOut8)
g_pGridMenu.add_command(label= 'Grid 32', command= GridZoomOut32())
g_pGridMenu.add_command(label= 'Grid 64', command= GridZoomOut64)
g_pGridMenu.add_command(label= 'Grid 81', command= GridZoomOut81)
g_pGridMenu.add_command(label= 'Grid 128', command= GridZoomOut128)
g_pGridMenu.add_command(label= 'Grid 164', command= GridZoomOut164)
g_pGridMenu.add_separator()
g_pGridMenu.add_command(label= 'Draw New Brush', command= RealRECT_Draw)
g_pGridMenu.add_separator()
g_pGridMenu.add_command(label = 'Snap to grid')
g_pGridMenu.add_separator()
g_pGridMenu.add_command(label= 'Reset Grid Type')
g_pMenuBar.add_cascade(label= 'Grid', menu= g_pGridMenu)

g_pWorkzoneMenu = gp.tk.Menu(g_pMenuBar)
g_pWorkzoneMenu.add_command(label= 'Workzone Enable')
g_pMenuBar.add_cascade(label= 'Workzone', menu= g_pWorkzoneMenu)

g_pConstructionZoneMenu = gp.tk.Menu(g_pMenuBar)
g_pConstructionZoneMenu.add_command(label= 'Brush Construction', command= CamWnd.BrushConstructionZone)
g_pMenuBar.add_cascade(label= 'Construction Zone', menu= g_pConstructionZoneMenu)

g_pRunMenu = gp.tk.Menu(g_pMenuBar)
g_pRunMenu.add_command(label= 'Simulate', command= CreateSimulationWindow)
g_pMenuBar.add_cascade(label= 'Run', menu= g_pRunMenu)

Global.GlobalOutputStream('---Menu working---')
##uncrustified
##Global.GlobalOutputStream('function : Global.GlobalOutputStream() == '', does not work nor print strings, UPDATE : CHANGED CODE NOW WORKS! Just differently')
Global.GlobalOutputStream('---Application Running---')

#==========================
# print grid types data

#just reference code
##g_pSplashImage = gp.tk.PhotoImage(name='SPLASH', master=g_pSplashScreen , format = 'PNG', file = 'app\esp_splash_logo' + '.png')

def XYPrint():
   #currents
   xCurr = XYWnd.xCur
   yCurr = XYWnd.yCur
   CurXPos = XYWnd.xPos
   CurYPos = XYWnd.yPos
   #buffering
   pXYStringBuffer = [2048]
   
   bXYDragged = XYWnd.bDragged = True or False
   
   XYWnd.mWidth = gp.w
   XYWnd.mHeight = gp.h
   XYWnd.mRows and XYWnd.mColumns == gp.ratio
   
   set().add(XYWnd.viewtype)
   XYWnd.viewtype == gp.PLANE_X and gp.PLANE_Y
   
   XYWnd.XYSetWnd(g_pXYWnd)
   
   XYWnd.xyvec3_t == [0.0, 0.0, 0.0]
   ##XYWnd.mXYMatrix == 16##uncrustify later
   
   ##wrestled with this xy_icon rendering issues for about a solid 2 hours, praise the Lord I figured out
   #note : have to call the <master=> func or else image wont bind to grid view
   xy_icon = PhotoImage(master= g_pXYWnd)
   g_pXYWnd.create_image(345, 165, image= xy_icon)
   
   g_pXYWnd.xy_icon = xy_icon
   
   #call dimension print
   XYDimensionsPrint()
   
   Global.GlobalOutputStream('XYPrint(()->g_pXYWnd)::Successfull')
 
XYPrint()

#============================
#   XZ Print()
def XZPrint():
    
    xCurr = XZWnd.xCur
    yCurr = XZWnd.yCur
    CurXPos = XZWnd.xPos
    CurYPos = XZWnd.yPos
   #buffering
    pXYBuff = str = [2048]
   
    bXZDragged = XZWnd.bDragged = True or False
   
    XZWnd.mWidth = gp.w
    XZWnd.mHeight = gp.h
    XZWnd.mRows and XZWnd.mColumns == gp.ratio
   
    set().add(XZWnd.viewtype)
    XZWnd.viewtype == gp.PLANE_X and gp.PLANE_Z
   
    XZWnd.XZSetWnd(g_pXZWnd)
    
    #now call print dimensions function
    XZDimensionsPrint()
   
    XZWnd.xzvec3_t == [0.0, 0.0, 0.0]
    
    #****************************************************************************
    xz_icon = PhotoImage(master= g_pXZWnd)
    g_pXZWnd.create_image(345, 165, image= xz_icon)
    
    g_pXZWnd.xz_icon = xz_icon
    
    Global.GlobalOutputStream('XZPrint(()->g_pXZWnd)::Successfull')
   
XZPrint()

#============================
#   YZ print() 
def YZPrint():
    
    xCurr = YZWnd.xCur
    yCurr = YZWnd.yCur
    CurXPos = YZWnd.xPos
    CurYPos = YZWnd.yPos
   #buffering
    pXYBuff = str = [2048]
   
    bYZDragged = YZWnd.bDragged = True or False
   
    YZWnd.mWidth = gp.w
    YZWnd.mHeight = gp.h
    YZWnd.mRows and YZWnd.mColumns == gp.ratio
   
    set().add(YZWnd.viewtype)
    YZWnd.viewtype == gp.PLANE_Y and gp.PLANE_Z
   
    YZWnd.YZSetWnd(g_pYZWnd)
   
    YZWnd.yzvec3_t == [0.0, 0.0, 0.0]
    
    
    #**********************************************************************
    yz_icon = PhotoImage(master= g_pYZWnd)
    g_pYZWnd.create_image(345, 165, image= yz_icon)
    
    #now call print dimensions function
    YZDimensionsPrint()
    
    g_pYZWnd.yz_icon = yz_icon
    
    Global.GlobalOutputStream('YZPrint(()->g_pYZWnd)::Successfull')
   
YZPrint()

#testing...
#compiled but no face shows in the viewport
#DummyFaceDraw()
#hmm i'll do more work later, im in a rush

g_pMainFrame.mainloop()
