from pygame import *

"""Classes."""
class GameSprite(sprite.Sprite):
    '''конструктор класса'''
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        '''каждый спрайт хранит прямоугольник rect, в который вписан'''
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        '''метод, отрисовывающий героя на окне'''
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    '''класс главного игрока'''
    def update_r(self):
        '''движение'''
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_l(self):
        '''движение'''
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

"""Main window."""
back = (246, 187, 131)
win_width = 600
win_height = 500
display.set_caption("Ping-Pong")
window = display.set_mode((win_width, win_height))
window.fill(back)

"""Flags."""
game = True
finish = False
#clock = time.Clock()
FPS = 60

"""Ball and rackets for game."""
racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = GameSprite("tenis_ball.png", 200, 200, 4 , 50, 50)

"Fonts."
font.init()
font = font.Font("Font_write.ttf", 35)
lose1 = font.render("Player 1 lost.", True, (180, 0, 0))
lose2 = font.render("Player 2 lost.", True, (180, 0, 0))

"""Cycle."""
speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y















