"""
Un arbre gran enmig
"""
#maria nicolau jaume

import arcade

def arbre (px,py):
    arcade.draw_lrtb_rectangle_filled(px, px+35, 100+py, py, arcade.csscolor.BROWN)
    arcade.draw_circle_filled(5+px, 140+py, 40, arcade.csscolor.GREEN)
    arcade.draw_circle_filled(15+px, 130+py, 40, arcade.csscolor.GREEN)
    arcade.draw_circle_filled(30+px, 140+py, 40, arcade.csscolor.GREEN)
    arcade.draw_circle_filled(20+px, 145+py, 40, arcade.csscolor.GREEN)
    arcade.draw_circle_filled(20+px, 135+py, 4, arcade.csscolor.PINK)
    arcade.draw_circle_filled(40+px, 155+py, 4, arcade.csscolor.PINK)
    arcade.draw_circle_filled(40+px, 120+py, 4, arcade.csscolor.PINK)
    arcade.draw_circle_filled(1+px, 155+py, 4, arcade.csscolor.PINK)
    arcade.draw_circle_filled(1+px, 120+py, 4, arcade.csscolor.PINK)
def nuvol (px,py):
    arcade.draw_circle_filled(350+px, 320+py, 30, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(320+px, 310+py, 30, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(290+px, 320+py, 30, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(320+px, 330+py, 30, arcade.csscolor.WHITE)
def sol (px,py):
    arcade.draw_circle_filled(20+px, 360+py, 30, arcade.csscolor.YELLOW)

arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()

#Rectangles: 
arcade.draw_lrtb_rectangle_filled(0, 599, 100, 0, arcade.csscolor.LIGHT_GREEN)

arbre(100,100)
arbre(450,100)
nuvol(100,100)
sol(100,100)

"""
#Cercles: 

"""
# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
