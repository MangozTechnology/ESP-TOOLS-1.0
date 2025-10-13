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

from directory import AppFileDirectory as g_impAppDir
from directory import File as g_impFile

g_sTexturePath = 'ESP32//shader//'
g_pClipShader = g_impFile.FileName = 'Clip_Robot.png'

def LoadTexturesDirectory():
    g_impAppDir.FolderDirectory = g_sTexturePath
    for i in range(0):
        g_impAppDir.FolderName = 'shader'
        