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

"""
MAY NOT USE THIS FILE ANYMORE
*UNCRUSTIFY*
"""

g_fGrid_width = int
g_fGrid_height = int
g_fGrid_interval = int

Grid = tk.Canvas()


#zoom in function
def ZoomIn(Grid, g_fGrid_width, g_fGrid_height, g_fGrid_interval):
     for x in range(0, g_fGrid_width, g_fGrid_interval):
        Grid.create_line(x, 0, x, g_fGrid_height, fill="blue")
    # Draw horizontal lines
        for y in range(0, g_fGrid_height, g_fGrid_interval):
            Grid.create_line(0, y, g_fGrid_width, y, fill="blue")

#zoom out function
def ZoomOut(Grid, g_fGrid_interval):
    g_fGrid_interval = 10

ss_fGridStipple = str

gridscale = float

drag_grid = bool

def DragGrid()-> bool:
    drag_grid = True


class GridDrawQue():
    
    def GridDrawBlock(Grid):
        m_Width = 800
        m_Height = 1000
        m_Spacing = 383
        m_LineThickness = 2#thickness of grid block line

        for i in range(0, m_Width, m_Spacing):
            Grid.create_line(383, 0, 383, m_Height, fill= "gray", width= m_LineThickness)
        for j in range(0, m_Height, m_Spacing):
            Grid.create_line(0, 218, m_Width, 218, fill= "gray", width= m_LineThickness)
        
        
        