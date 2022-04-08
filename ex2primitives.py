"""
DIBUIXA AL QUADERN UN DISSENY D’UN ARBRE AMB VARIES COPES.
"""
#maria nicolau jaume

import arcade

#Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

#Rectangles: 
arcade.draw_lrtb_rectangle_filled(0, 599, 250, 0, arcade.csscolor.LIGHT_GREEN)
arcade.draw_lrtb_rectangle_filled(200, 210, 270, 220, arcade.csscolor.BROWN)
#Cercles: 
arcade.draw_circle_filled(205, 290, 30, arcade.csscolor.DARK_GREEN)
arcade.draw_circle_filled(180, 300, 30, arcade.csscolor.DARK_GREEN)
arcade.draw_circle_filled(223, 300, 30, arcade.csscolor.DARK_GREEN)
arcade.draw_circle_filled(200, 320, 30, arcade.csscolor.DARK_GREEN)
arcade.draw_circle_filled(350, 520, 30, arcade.csscolor.WHITE)
arcade.draw_circle_filled(320, 510, 30, arcade.csscolor.WHITE)
arcade.draw_circle_filled(290, 520, 30, arcade.csscolor.WHITE)
arcade.draw_circle_filled(320, 530, 30, arcade.csscolor.WHITE)
# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()