
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

import tkinter as widget

def CreateSimulationWindow():
    Window = widget.Tk()
    Window.title('Simulation')
    Window.configure(relief= 'sunken', bd= 1, bg= 'Grey')
    
    Window.mainloop()