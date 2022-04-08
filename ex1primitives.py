"""
FES QUATRE QUADRATS DE DIFERENTS COLORS QUE, entre tots, OCUPIN TOTA LA PANTALLA.
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
arcade.draw_lrtb_rectangle_filled(0, 300, 300, 0, arcade.csscolor.LIGHT_GREEN)
arcade.draw_lrtb_rectangle_filled(300, 600, 300, 0, arcade.csscolor.LIGHT_BLUE)
arcade.draw_lrtb_rectangle_filled(0, 300, 600, 300, arcade.csscolor.PINK)
arcade.draw_lrtb_rectangle_filled(300, 600, 600, 300, arcade.csscolor.ORANGE)
# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()