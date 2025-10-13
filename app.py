
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

g_pMainFrame = gp.GuiTable.MainWindow
g_pMainFrame.title('ESP Editor - Version 1.0 ( Fall 2025 )')

#=========================
#   Global Widgets

g_pMenuBar = gp.tk.Menu(g_pMainFrame, type= 'menubar')
g_pFileMenu = gp.tk.Menu(g_pMenuBar)
g_pMenuBar.configure(bg= 'black')
g_pFileMenu.add_command(label= 'New ESP Map')
g_pFileMenu.add_command(label= 'Open ESP Map')
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
g_pTextureMenu.add_command(label= 'Shader')
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
g_pRenderMenu.add_command(label= 'Wireframe')
g_pRenderMenu.add_command(label= 'Full')
g_pRenderMenu.add_command(label= 'Fake')
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
g_pBkgrndMenu.add_command(label= 'New Bkgrnd Image')
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

#NewBrush_DragEvent = g_pXYWnd.bind("<Button-1>")

def RealRECT_Draw():
        gp.GridDrawRectangle(g_pXYWnd)
        gp.GridDrawRectangle(g_pXZWnd)
        gp.GridDrawRectangle(g_pYZWnd)

g_fGridWidth = 1000
g_fGridHeight = 1000
g_fGridRatio = 20

prev_grd = gp.tk.Canvas()

def CallBackPrevGrid(prev_grd):
    return prev_grd

def ClearPrevLines():
    del g_fGridRatio
    
def GridZoomOut8():
    zoomRatio = 8
    
    gp.PaintXYGrid(g_pXYWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    gp.PaintXYGrid(g_pXZWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    gp.PaintXYGrid(g_pYZWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    
def GridZoomOut32():
    zoomRatio = 24
    
    gp.PaintXYGrid(g_pXYWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    gp.PaintXYGrid(g_pXZWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    gp.PaintXYGrid(g_pYZWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    
    
def GridZoomOut64():
    zoomRatio = 64
    
    gp.PaintXYGrid(g_pXYWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    gp.PaintXYGrid(g_pXZWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    gp.PaintXYGrid(g_pYZWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    
def GridZoomOut81():
    zoomRatio = 81
    
    gp.PaintXYGrid(g_pXYWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    gp.PaintXYGrid(g_pXZWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    gp.PaintXYGrid(g_pYZWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    
def GridZoomOut128():
    zoomRatio = 128
    
    gp.PaintXYGrid(g_pXYWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    gp.PaintXYGrid(g_pXZWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    gp.PaintXYGrid(g_pYZWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    
def GridZoomOut164():
    zoomRatio = 164
    
    gp.PaintXYGrid(g_pXYWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    gp.PaintXYGrid(g_pXZWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    gp.PaintXYGrid(g_pYZWnd, g_fGridWidth, g_fGridHeight, zoomRatio)
    

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
   
g_pGridMenu = gp.tk.Menu(g_pMenuBar)
g_pGridMenu.add_command(label= 'Grid 8',command= GridZoomOut8)
g_pGridMenu.add_command(label= 'Grid 32', command= GridZoomOut32)
g_pGridMenu.add_command(label= 'Grid 64', command= GridZoomOut64)
g_pGridMenu.add_command(label= 'Grid 81', command= GridZoomOut81)
g_pGridMenu.add_command(label= 'Grid 128', command= GridZoomOut128)
g_pGridMenu.add_command(label= 'Grid 164', command= GridZoomOut164)
g_pGridMenu.add_separator()
g_pGridMenu.add_command(label= 'Draw New Brush', command= RealRECT_Draw)
g_pGridMenu.add_separator()
g_pGridMenu.add_command(label = 'Snap to grid')
g_pGridMenu.add_separator()
g_pGridMenu.add_command(label= 'Reset Grid Type' )
g_pMenuBar.add_cascade(label= 'Grid', menu= g_pGridMenu)

g_pWorkzoneMenu = gp.tk.Menu(g_pMenuBar)
g_pWorkzoneMenu.add_command(label= 'Workzone Enable')
g_pMenuBar.add_cascade(label= 'Workzone', menu= g_pWorkzoneMenu)

g_pConstructionZoneMenu = gp.tk.Menu(g_pMenuBar)
g_pConstructionZoneMenu.add_command(label= 'Construction Zone View')
g_pConstructionZoneMenu.add_command(label= 'Brush Construction')
g_pMenuBar.add_cascade(label= 'Construction Zone', menu= g_pConstructionZoneMenu)

print('---Menu working---')
print('---Application Running---')

g_pMainFrame.mainloop()
