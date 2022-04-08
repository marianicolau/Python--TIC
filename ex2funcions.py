"""
Exercici 2, funcions
Fes que desde main es dibuixin 6 arbres en posicions aleatories i mida “estudiada”.
"""
#maria nicolau jaume
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

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


def dibuixaArbres(nombre,py):
    max = SCREEN_WIDTH
    espai = max / nombre
    print(espai)
    x = 0 - 100
    for i in range(nombre):
        x += espai
        print("x",x)
        arbre(x,py)

def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.LIGHT_GREEN)


def draw_snow_person(x, y, e):
    """ Draw a snow person """

    # Snow
    arcade.draw_circle_filled(x+70*e, 50 + y-100*e, 40*e, arcade.color.WHITE)
    arcade.draw_circle_filled(x+70*e, 100 + y-100*e, 30*e, arcade.color.WHITE)
    arcade.draw_circle_filled(x+70*e, 150 + y-100*e, 25*e, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x+70 - 15*e, 155 + y-100*e, 4*e, arcade.color.BLACK)
    arcade.draw_circle_filled(x+70 + 15*e, 155 + y-100*e, 4*e, arcade.color.BLACK)
    
    # Nas
    arcade.draw_circle_filled(x+70*e, 145 + y-100*e, 4*e, arcade.color.ORANGE)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    arcade.start_render()

    draw_grass()
    dibuixaArbres(6,200)
    draw_snow_person(50, 180, 1)
    draw_snow_person(180, 180, 1)
    draw_snow_person(310, 180, 1)
    draw_snow_person(440, 180, 1)
    draw_snow_person(570, 180, 1)
    
    # Finish and run
    arcade.finish_render()
    arcade.run()

# Call the main function to get the program started.
main()