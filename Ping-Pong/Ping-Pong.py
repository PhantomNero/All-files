from pygame import *

"""Main window."""
win_width = 700
win_height = 500
display.set_caption("Ping-Pong")
window = display.set_mode((win_width, win_height))

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


