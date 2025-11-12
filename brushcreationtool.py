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

"""
 Brush Creation Tool
 similar functions to this in other files
"""
from brushwindings import BrushWindings
from stdafx import GuiTable

class BrushCreationTool:
    
    #this is it... maybe
    def createBrush():
        #creates a huge winding brush...
        BrushWindings.BrushWindingHuge(windingBrushNode= BrushWindings.windingBrushNode, brushWinding= BrushWindings.brushWinding)
        
    # A brush constructed strictly coords, no face, no planes, no vertices
    # mins and maxs coords
    # this is mainly for testing
    def constructCuboid(mins, maxs):
        mins = [-10.0, -30.0, -100.0, -60.0, -80.0, -20.0, -5.0, -100.0, -120.0, -130.0, -140.0, -160.0, -170.0, -180.0, -190.0, -110.0]
        maxs = [100.0, 500.0, 300.0, 500.0, 700.0, 300.0, 300.0, 120.0, 130.0, 140.0, 150.0, 160.0, 170.0, 180.0, 190.0, 200.0]
        
        #auto caulk cuboid
        brushCaulkAuto = 'Caulk.png'
        
        # implement rendering code
        # Coordinates for the cuboid
        # Front face (rectangle)
        x, y = 100, 100
        w, h = 120, 80
        d = 40  # depth offset

        # Points of the cuboid
        # Front face
        front_top_left     = (x, y)
        front_top_right    = (x + w, y)
        front_bottom_right = (x + w, y + h)
        front_bottom_left  = (x, y + h)

        # Back face (shifted by depth)
        back_top_left     = (x + d, y - d)
        back_top_right    = (x + w + d, y - d)
        back_bottom_right = (x + w + d, y + h - d)
        back_bottom_left  = (x + d, y + h - d)

        # Draw faces using create_polygon
        # Top face
        # Side face

        GuiTable.m_pXYWidget.create_polygon(front_top_left, front_top_right, back_top_right, back_top_left, fill= '', outline= 'red', width= 2)
        GuiTable.m_pXZWidget.create_polygon(front_top_left, front_top_right, front_bottom_right, front_bottom_left, fill= '', outline= 'red', width= 2)
        GuiTable.m_pYZWidget.create_polygon(front_top_right, front_bottom_right, back_bottom_right, back_top_right, fill= '', outline= 'red', width= 2)