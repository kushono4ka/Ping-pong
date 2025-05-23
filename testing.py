from pygame import *
from random import randint
init()

class GameSprite(sprite.Sprite): 
    def __init__(self, player_image, player_x, player_y, size_w, size_h, player_speed): 
        super().__init__() 
        self.image = transform.scale(image.load(player_image), (size_w, size_h)) 
        self.speed = player_speed  
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y)) 

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 600-80:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 600-80:
            self.rect.y += self.speed


window = display.set_mode((900, 600))
display.set_caption("Ping-Pong")
background = transform.scale(image.load("wallpaper.png"),(900, 600))

rocket_right = Player1("ping_rocket.png", 870, 270, 20, 110, 10)
rocket_left = Player2("ping_rocket.png", 20, 270, 20, 110, 10)
ball = GameSprite("ball.png", 450, 100, 35, 35, 15)


font.init()
font1 = font.SysFont('Arial', 35)

Game = True
finish = False
while Game:
    for e in event.get():
        if e.type == QUIT:
            Game = False
    
    if not finish:
        window.blit(background, (0, 0))
        rocket_left.update()
        rocket_right.update()

    ball.reset()
    rocket_left.reset()
    rocket_right.reset()


    display.update()
    time.delay(30)