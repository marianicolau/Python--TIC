#dibuix ninot de neu i arbre

import arcade

def ninot (px,py):
    #cos
    arcade.draw_circle_filled(100+px, 100+py, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(100+px, 170+py, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(100+px, 240+py, 40, arcade.color.WHITE)
    #ulls i nas
    arcade.draw_circle_filled(80+px, 250+py, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(120+px, 250+py, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(100+px, 230+py, 5, arcade.color.ORANGE)
    #botons
    arcade.draw_circle_filled(100+px, 100+py, 5, arcade.color.BROWN)
    arcade.draw_circle_filled(100+px, 140+py, 5, arcade.color.BROWN)
    arcade.draw_circle_filled(100+px, 180+py, 5, arcade.color.BROWN)
    #bufanda
    arcade.draw_lrtb_rectangle_filled(60+px, 140+px, 215+py, 200+py, arcade.csscolor.PINK)
    arcade.draw_lrtb_rectangle_filled(125+px, 140+px, 215+py, 150+py, arcade.csscolor.PINK)
    #capell
    arcade.draw_lrtb_rectangle_filled(70+px, 130+px, 300+py, 260+py, arcade.csscolor.BLACK)
    arcade.draw_lrtb_rectangle_filled(50+px, 150+px, 270+py, 260+py, arcade.csscolor.BLACK)
def arbre (px,py):
    #tronc
    arcade.draw_lrtb_rectangle_filled(285+px, 315+px, 160+py,0+py, arcade.csscolor.BROWN)
    #fulles
    arcade.draw_triangle_filled(300+px, 450+py, 190+px, 60+py, 410+px, 60+py, arcade.csscolor.GREEN)
    arcade.draw_triangle_filled(300+px, 450+py, 200+px, 160+py, 390+px, 160+py, arcade.csscolor.GREEN)
    arcade.draw_triangle_filled(300+px, 500+py, 210+px, 230+py, 380+px, 230+py, arcade.csscolor.GREEN)
def nuvol (px,py):
    arcade.draw_circle_filled(px, py, 40, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(40+px, -20+py, 30, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(55+px, 30+py, 40, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(60+px, 25+py, 40, arcade.csscolor.WHITE)
    
arcade.open_window(600, 600, "Drawing Example")

# background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()

ninot(0,0)
arbre(100,0)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
