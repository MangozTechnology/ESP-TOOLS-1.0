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

def DrawTextureWindow():
    Window = tk.Tk()
    Window.title('Texture Window')
    
    TexView = tk.Listbox(Window, bg= 'DarkGray', relief= 'sunken', width= Window.winfo_width(), height= Window.winfo_height())
    TexView.pack(fill= 'both')
    
    Window.mainloop()