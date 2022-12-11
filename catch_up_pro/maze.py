# создай игру "Лабиринт"!
import time

from pygame import *


class GameSprite(sprite.Sprite):
    """Родительский клсс."""

    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (80, 80))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    """Класс для спрайта-игрока."""
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 440:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        if self.direction == "right":
            self.rect.x += self.speed

class Enemy2(GameSprite):
    direction = "down"
    def update(self):
        if self.rect.y <= 190:
            self.direction = "up"
        if self.rect.y >= win_height - 85:
            self.direction = "down"

        if self.direction == "down":
            self.rect.y -= self.speed
        if self.direction == "up":
            self.rect.y += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wall_width
        self.height = wall_height
        """картинка стены - прямоугольник нужных размеров и цвета."""
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        draw.rect(window,
                  (self.color1, self.color2, self.color3),
                  (self.rect.x, self.rect.y, self.width, self.height)
                  )
w1 = Wall(158, 206, 45, 10, 20, 680, 10)
w2 = Wall(158, 206, 45, 110, 480, 450, 10)
w3 = Wall(158, 206, 45, 100, 20, 10, 320)
w4 = Wall(158, 206, 45, 260, 300, 300, 10)
w5 = Wall(158, 206, 45, 110, 150, 300, 10)
w6 = Wall(158, 206, 45, 550, 170, 10, 310)


"""Игровая сцена"""
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Лабиринт.")
background = transform.scale(image.load("background.jpg"), (700, 500))

"""Музыка."""
mixer.init()
mixer.music.load("jungles.mp3")
mixer.music.play()
money = mixer.Sound("money.ogg")
kick = mixer.Sound("kick.ogg")

"""Персонажи игр."""
player = Player("monkey.png", 5, win_height - 100, 3)
monster = Enemy("gorila.png", win_width - 100, 200, 2)
final = GameSprite("banana.png", win_width - 130, win_height - 100, 0)
monster2 = Enemy2("14-1.png", win_width - 400, 200, 2)

game = True
finish = False
clock = time.Clock()
FPS = 60

"""Шрифты"""
font.init()
font = font.Font(None, 70)
win = font.render("     Победа", True, (236,220, 57))
lose = font.render("Поражение", True, (221,101,57))

"""Игровой цикл."""
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:

        window.blit(background, (0, 0))
        player.update()
        monster.update()
        monster2.update()

        player.reset()
        monster.reset()
        final.reset()
        monster2.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()

    if sprite.collide_rect(player, monster) or sprite.collide_rect(player,w1) or sprite.collide_rect(player,w2) or sprite.collide_rect(player,w3) or sprite.collide_rect(player,w4) or sprite.collide_rect(player,w5) or sprite.collide_rect(player,w6) or sprite.collide_rect(player, monster2):
        finish = True
        window.blit(lose, (200, 200))
        kick.play()



    if sprite.collide_rect(player, final):
        finish = True
        window.blit(win, (200, 200))
        money.play()

    display.update()
    clock.tick(FPS)

#https://www.8host.com/blog/operatory-break-continue-i-pass-v-ciklax-python-3/