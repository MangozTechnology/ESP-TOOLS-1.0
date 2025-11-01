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
import mathvec as vec_t

#Panel
#ClientViewport = tk.PanedWindow

class Viewport():
    bShowCrosshair = bool

   ### moved to camera window code
   ### x = vec_t.vec3_f = { 0.0, 0.0, 0.0 }
   ### y = vec_t.vec3_f = { 0.0, 0.0, 0.0 }
   ### z = vec_t.vec3_f = { 0.0, 0.0, 0.0 }

    ViewMode = int

    NoLighting = int
    Wireframe = int
    Cull = int
    Fill = int


#test regression polygons().for grid testing
def DrawPlane(XY):
    
   planeVectors = vec_t.vec3_f = [0.0, 1.0, 0.0]
   
   #draw plane lines
   m_Width = 600
   m_Height = 600
   m_Spacing = 400
   m_LineThickness = 3#thickness of grid block line

   for i in range(0, m_Width, m_Spacing):
        XY.create_line(13, 109, 129, 10, fill= "blue", width= m_LineThickness)
   for j in range(0, m_Height, m_Spacing):
        XY.create_line(200, 89, 13, 125, fill= "blue", width= m_LineThickness)
    
    
##dummy polygon test for camera window
def DrawPolygon(Camerawindow):
    Camerawindow.create_polygon(100, 300, 500, 200, 400, 450,  fill= "gray", outline= "black", width= 1)

