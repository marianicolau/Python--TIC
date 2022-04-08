"""
Exercici 1, funcions
Fes que desde main es dibuixin 6 ninots en posicions aleatories
"""
#maria nicolau jaume

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snow_person(x, y):
    """ Draw a snow person """

    # Snow
    arcade.draw_circle_filled(x, 50 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 100 + y, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 150 + y, 30, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 15, 155 + y, 4, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 155 + y, 4, arcade.color.BLACK)
    
    # Nas
    arcade.draw_circle_filled(x, 145 + y, 4, arcade.color.ORANGE)

    # Estrelles

    arcade.draw_circle_filled(x+60, 400 + y, 4, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 350 + y, 4, arcade.color.WHITE)
    arcade.draw_circle_filled(x+60, 300 + y, 4, arcade.color.WHITE)   
    arcade.draw_circle_filled(x, 250 + y, 4, arcade.color.WHITE)
    arcade.draw_circle_filled(x+60, 200 + y, 4, arcade.color.WHITE)

    # Bufanda
    arcade.draw_lrtb_rectangle_filled(x-30, x+30, 133+y, y+125, arcade.csscolor.PINK)
    arcade.draw_lrtb_rectangle_filled(x+13, x+20, 133+y, y+90, arcade.csscolor.PINK)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    draw_grass()
    draw_snow_person(50, 180)
    draw_snow_person(150, 180)
    draw_snow_person(250, 180)
    draw_snow_person(350, 180)
    draw_snow_person(450, 180)
    draw_snow_person(550, 180)
    draw_snow_person(650, 180)
    draw_snow_person(750, 180)

    # Finish and run
    arcade.finish_render()
    arcade.run()

# Call the main function to get the program started.
main()