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

    """
    DONT USE
    """
    def UpdatePanel(ClientViewport):
        for i in range(ClientViewport):
            Viewport.ViewMode
            Viewport.x
            Viewport.y
            Viewport.z




