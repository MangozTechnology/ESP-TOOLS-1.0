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

def DragGrid():
    drag_grid = True

def IncrementGrid():
    any()

def DecrementGrid():
    any()

#1024 buffer count

#for holding points and nodes in the grid
def GridEntityTable():
    any()

#
# USE GRK
#
def GridRenderPoint():
    any()

def GridRenderNode():
    any()

