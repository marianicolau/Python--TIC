import arcade
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Ball:
    """ This class manages a ball bouncing on the screen. """

    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        """ Constructor. """

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def xoc(self):
        self.change_x *= -1
        self.change_y *= -1

    def update(self):
        """ Code to control the ball's movement. """

        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.change_y *= -1

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1

def colisio(a,b):
    distancia = math.sqrt(math.pow((a.position_x - b.position_x),2) + math.pow((a.position_y - b.position_y),2))
    #print(distancia)
    if distancia <= (a.radius) + (b.radius):
        return True
    else:
        return False

class Floc(Ball):
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        super().__init__(position_x, position_y, change_x, change_y, radius, color)
    def update(self):
        """ Code to control the ball's movement. """

        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.position_y = SCREEN_HEIGHT 
            
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

def regal (px,py):
    arcade.draw_lrtb_rectangle_filled(px, 100+px, 100+py,py, arcade.csscolor.PINK)
    arcade.draw_lrtb_rectangle_filled(47+px, 53+px, 100+py,py, arcade.csscolor.RED)
    arcade.draw_lrtb_rectangle_filled(px, 100+px, 53+py,py+47, arcade.csscolor.RED)

def arbre (px,py):
    #tronc
    arcade.draw_lrtb_rectangle_filled(285+px, 315+px, 160+py,0+py, arcade.csscolor.BROWN)
    #fulles
    arcade.draw_triangle_filled(300+px, 450+py, 190+px, 60+py, 410+px, 60+py, arcade.csscolor.GREEN)
    arcade.draw_triangle_filled(300+px, 450+py, 200+px, 160+py, 390+px, 160+py, arcade.csscolor.GREEN)
    arcade.draw_triangle_filled(300+px, 500+py, 210+px, 230+py, 380+px, 230+py, arcade.csscolor.GREEN)
def nuvol (px,py,r):
    arcade.draw_circle_filled(px, py, r, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(px-30, py-10, r, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(px-60, py, r, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(px-30, py+10, r, arcade.csscolor.WHITE)

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Set the background color
        arcade.set_background_color(arcade.color.DARK_BLUE)

        self.llista = []
        
        px=0
        py=0

        for i in range(10):
            self.llista.append(Floc(random.randrange(px-50, px+80),random.randrange(-50, 50), 0,random.randrange(-3,-1), random.randrange(3, 4), arcade.color.WHITE))
            self.llista.append(Floc(random.randrange(px-60, px+90),random.randrange(-150, 150), 0, random.randrange(-3,-1), random.randrange(3, 4), arcade.color.WHITE))
            self.llista.append(Floc(random.randrange(px-70, px+100),random.randrange(-200, 200), 0, random.randrange(-3,-1), random.randrange(3, 4), arcade.color.WHITE))
            self.llista.append(Floc(random.randrange(px-80, px+120),random.randrange(-250,250), 0, random.randrange(-3,-1), random.randrange(3, 4), arcade.color.WHITE))
            self.llista.append(Floc(random.randrange(px-90, px+150),random.randrange(-300, 300), 0, random.randrange(-3,-1), random.randrange(3, 4), arcade.color.WHITE))
            self.llista.append(Floc(random.randrange(px-100, px+170),random.randrange(-350, 350), 0, random.randrange(-3,-1), random.randrange(3, 4), arcade.color.WHITE))
            px +=65
        

    
    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        nuvol(150,500,40)
        nuvol(450,500,30)
        nuvol(300,550,30)
        regal(400,0)
        arbre(30,0)
        ninot(20,-40)
        
        for i in self.llista:
            i.draw()
        

    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""
        for i in self.llista:
            i.update()

def main():
    window = MyGame(600, 600, "Drawing Example")

    arcade.run()

main()