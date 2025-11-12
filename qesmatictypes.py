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

#***imports***
from face import Face
from brush import Brush
from plane3 import Plane3
from aabb import AABB
from node import node
from polygon import Polygon
from global_stream import Global
from bsp import Bsp
from point import GridPoint
from stdafx import ReturnViewType
from stdafx import GuiTable
from mathvec import vec3_f as vec3_t
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox as dialog

EDITOR_VERSION = '1.0'


#*colors*
COLOR_GRID = 0xaa0
COLOR_BLOCK_GRID = 0xaa1
COLOR_ENTITY_GRID = 0xaa2
COLOR_TEXT_GRID = 0xaa3
COLOR_BACKGROUND = 0xbb0
COLOR_STIPPLE = 0xff0
COLOR_ARROW = 0xcc0

#entity visible???
bVisible = bool

FileBkgrndBrowsePath = str
FileBrowseMapPath = str
FileBrowseSimulationPath = str

def WXY_Paint():
    return

def WXZ_Paint():
    return

def WYZ_Paint():
    return

#grid arrow
ARROW = 0xDD0
ARROW_LOOP = 0xDD1
ARROW_LINE = 0xDD2

#=================================
AXIS_ALIGNED_BOUNDING_BOX = 0xEE0

#=================================
XY_UP = 0x0
XY_LEFT = 0x1
XY_DOWN = 0x2
XY_RIGHT = 0x3

def VendBrush(brush):
    return

def UpdateWindow(window):
    bits = int
    bits |= window
    
def RefInc(n):
    return n

def RefDec(n):
    return (n) == False

class QES_GlobalFaceTable:
    
    qes_global_FaceList = int
    qes_global_bSel = bool
    
    def PFN_GET_FACE(Face):
        any()
    def PFN_CREATE_FACE(Face, pnts, va, vb, vc, vd):
        any()
    def PFN_FACE_TEXTURE(Face, Texture):
        any()
    def PFN_SELECT_FACE(Face):
        any()
    def PFN_HIGHLIGHT_FACE(Face, Color):
        any()
        
class QES_GlobalBrushTable:
    
    qes_global_BrushList = int
    qes_global_bSel = bool
    
    def PFN_GET_BRUSH(Brush):
        any()
    def PFN_CREATE_BRUSH(Brush, min, max):
        any()
    def PFN_BRUSH_TEXTURE(Brush, Shader):
        any()
    def PFN_BRUSH_SELECT(Brush):
        any()
    def PFN_BRUSH_HIGHLIGHT(Brush, Color):
        any()
        
class QES_GlobalPlaneTable:
    
    qes_global_PlaneList = int
    qes_global_bSel = bool
    qes_global_PlaneType = int
    
    def PFN_CREATE_PLANE(Plane, va, vb, vc, pnts):
        any()
    def PFN_SELECT_PLANE(Plane):
        any()
    #need to fix this is proper winding
    def PFN_BASE_PLANE_WINDING(Winding_For_Plane):
        Winding_For_Plane == Plane3().Points

#================================
#=====short*keys=================
W_LITERAL = 'w' or 'W'
D_LITERAL = 'd' or 'D'
S_LITERAL = 's' or 'S'
CTRL_LITERAL = 'ctrl' or 'CTRL'

class QES_GlobalKeyTable:
    
    def PFN_GET_KEY(literal):
        return literal
    
def ProjectLine(line):
    any()
    
def ProjectPoint(point):
    any()

#Praise the Lord for my code!!!

#==================================================
def PlaneDrawXY(plane, viewtype):
    any()
    
def PlaneDrawXZ(plane, viewtype):
    any()
    
def PlaneDrawYZ(plane, viewtype):
    any()
    
def PlaneDrawViewport(plane, viewport):
    any()
    
def FaceDrawXY(face, viewtype):
    any()
    
def FaceDrawXZ(face, viewtype):
    any()
    
def FaceDrawYZ(face, viewtype):
    any()
    
def FaceDrawViewport(face, viewport):
    any()

#def BrushDrawXY(brush, viewtype):
 #   any()
    
def BrushDrawXZ(brush, viewtype):
    any()
    
def BrushDrawYZ(brush, viewtype):
    any()
    
def BrushDrawViewport(brush, viewport):
    any()

#==================================================
def DrawEntityXY(entity, viewtype):
    any()
    
def DrawEntityXZ(entity, viewtype):
    any()
    
def DrawEntityYZ(entity, viewtype):
    any()
    
def DrawEntityViewport(entity, viewport):
    any()
    
    
#==================================================
def ViewportCompressTexture(viewport, texture):
    any()
    
def ViewportProjectTexture(viewport, texture):
    any()

#===================================================
g_cESPMapFileName = str

g_cESPMapDirectory = r"C:\\_MAXNEW_CODE\\installs\\maps"

# Use ( g_cESPMapFileName ) or Whatever variable you want, I guess...
def LoadEspMap( map ):
    return map

def CloseEspMap( map ):
    return (map) == False

"""
    *!File types that are maps for the ESMatic app are , *.espmap or *.espbsp, only these files are supported for map formats!*
"""
def OpenMapDialog():
    open_map = filedialog.askopenfilename(title= "Open ESP Map", filetypes=[("*.espmap", "*.espmap"), ("*.espbsp", "*.espbsp")])
    if open_map:
        #now load the map
        LoadEspMap(open_map)
        #change the title of the app to the name of the map that was loaded
        GuiTable.MainWindow.title(open_map)
        #I will fix printing later
        Global.GlobalOutputStream('Opened {$open_map}...')
        

#===================================================
# For buffering the XY, XZ and YZ Windows
# Viewtype can match buffer which could switch viewtype properly in a different method
zBuffer = int
xBuffer = int
yBuffer = int

#===================================================
imagebuffer = int
imageunsignedcode = str
imageaddress = int

#===================================================
AppIcon = "esmatic_icon.png"
AppIconBuffer = int
NewIconAddress = int

#===================================================

def load_image(img):
   if ( img )== True:                           #unpack image
    open(img, 'r+', 1024, None, None, 1, False)(*img)
    
def load_pic(pic):
    if( pic ) == True:                         #unpack picture
        open(pic, 'r+', 1024, None, None, 1, False)(*pic)
        
#===================================================
class Side:
    BrushSide = Face
    brushSideCount = 6
    brushSideSelect = bool
    
    def SideOnXY(side)-> bool:
        if side.BrushSide.facepnts == ReturnViewType(viewtype= XY_UP):
            return True
        else:
            return False
    
    def SideOnXZ(side)->bool:
        if side.BrushSide.facepnts == ReturnViewType(viewtype= XY_LEFT):
            return True
        else:
            return False
        
    def SideOnYZ(side)->bool:
        if side.BrushSide.facepnts == ReturnViewType(viewtype= XY_RIGHT):
            return True
        else:
            return False

def Construct(_type):
    any()
    
def getAny(any):
    return any

#=========================================

def Get_ESPExtension()->str:
    return "espmap"

#============================================
#used for parsing and writing file formats
class LiteralType:
    period = '.'
    asterik = '*'
    comma = ','
    lparen = '('
    rparen = ')'
    slash = '/'
    question = '?'
    
    
#==============================================
#   Highlighter utility code...
#   Used for Brush or Face Selection
SELECTION_HIGHLIGHTER_COLOR_RED = "#FF2A3167"
SELECTION_HIGHLIGHTER_COLOR_GREEN = "#67FF2B7C"
SELECTION_HIGHLIGHTER_COLOR_BLUE = "#0071E299"
    

#===============================================
#           Mouse Buttons Events

def MouseButtonUp(mb):
    any()
    
def MouseButtonDown(mb):
   any() 
    
def MouseButtonLeft(mb):
    any()
    
def MouseButtonRight(mb):
    any()
    
def UpdateWindowForMouseButtonEvent(mb, widget):
    any()
    
class RobotEntity:
    
    roboId = int
    bConnected = bool
    
    def Robot_Info(robocode)->str:
        return robocode
    
    def DrawRobotIcon():
        any()
    
#==============================================
class PathNode(node):
    bnodeId = 0
    pos = vec3_t
    
    bInSimualtionMode = bool
    
    script = str
    
    #robot only goes to postion while in simulation
    def RobotGotToNewPosition(robot, position):
        robot.pos == position
    
    brushnode = Brush()#construct brush node
    
    def AddBrushNodeToScene(scene, brushnode):
        scene = GuiTable.m_pCamWidget
        QESGlobalEvent.Hook(scene)
        BrushDrawViewport(brush= brushnode, viewport= scene)
        UpdateWindow(scene)
        
        
def QES_Error_Printf(message):
    print(message)

class QESGlobalEvent():
    
    #be careful using this function it automatically packs the window so positions are not really 
    def PaintWindow(window):
        window.pack()
    def CallPaintWindow(any):
        QESGlobalEvent.PaintWindow(any)
    def CallListUpdate(any):
        return
    def Hook(window):
        getattr(window)

class QESGlobals:
    bBrushSelMode = bool
    bBrushIsSel = bool
    
    bResizeWindow = bool
    
    d_globals_grid_size = float
    d_globals_brush_scale = float
    d_globals_celi = float
    d_globals_floor = float
    d_globals_sel_shader = str
  
#globals pointer  
g_qesglobals = QESGlobals
g_qesglobalevent = QESGlobalEvent

#=========================================
def XYDimensionsPrint():
    _xy = GuiTable.m_pXYWidget
    dimensions_ = "0        64          128         164         512         1024        2048        3026"
    _xy.create_text(350, 7, anchor= 'n', text= dimensions_, font= ("Consolas", 12), fill = "black" )
    
def XZDimensionsPrint():
    _xz = GuiTable.m_pXZWidget
    dimensions_ = "0        64          128         164         512         1024        2048        3026"
    _xz.create_text(350, 7, anchor= 'n', text= dimensions_, font= ("Consolas", 12), fill = "black" )
    
def YZDimensionsPrint():
    _yz = GuiTable.m_pYZWidget
    dimensions_ = "0        64          128         164         512         1024        2048        3026"
    _yz.create_text(350, 7, anchor= 'n', text= dimensions_, font= ("Consolas", 12), fill = "black" )

#=========================================
def drag_clck_rel():
    Global.GlobalOutputStream('Drag-Click-Release-Mouse Tool...')

#===============================
# mosue bindings are so difficult and hard I cant manage to get them to work
def XYDraw_EventFailed():
        m_pXYWnd = GuiTable.m_pXYWidget
        xyMouseEvent = m_pXYWnd.bind(sequence= "<Button-1>")
        drag_clck_rel()
        
        if xyMouseEvent:
            xyDialog = dialog.showerror('XY Error', message= 'XY Draw Brush Event Failed.', icon= 'error')
            
        
#=============================================================
#           PEN DRAWING
            


