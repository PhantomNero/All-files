# Создай собственный Шутер!
from time import time as timer
from random import randint
from pygame import *

'''картинки'''
img_back = 'galaxy.jpg'  # фон игры
img_hero = 'rocket.png'  # герой
img_enemy = 'ufo.png'  # враг
img_bullet = 'bullet.png'  # пуля

'''счётчики сбитых и пропущенных кораблей'''
score = 0
lost = 0
max_lost = 3
goal = 100
life = 3

'''создаём игровое окно'''
win_width = 700
win_height = 500
display.set_caption('Космический блокбастер')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

'''фоновая музыка'''
mixer.init()
mixer.music.load('space.mp3')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

'''шрифты и надписи'''
font.init()
font1 = font.Font(None, 80)
win = font1.render('ПОБЕДА', True, (194, 185, 37))
lose = font1.render('ВЫ ПРОИГРАЛИ', True, (238, 138, 137))
font2 = font.Font(None, 36)

'''класс-родитель для других спрайтов'''


class GameSprite(sprite.Sprite):
    '''конструктор класса'''

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
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

    def update(self):
        '''движение'''
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    def fire(self):
        '''выстрел'''
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)


class Enemy(GameSprite):
    '''движение врага:'''

    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost += 1


class Asteroid(GameSprite):
    '''астероид'''

    def update(self):
        '''движение астероида'''
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0


class Bullet(GameSprite):
    '''класс спрайта-пули'''

    def update(self):
        '''движение врага'''
        self.rect.y += self.speed
        if self.rect.y < 0:
            '''исчезает, если дойдёт до края экрана'''
            self.kill()


'''создаём спрайты'''
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)

asteroids = sprite.Group()
for i in range(1, 3):
    asteroid = Asteroid('asteroid.png', randint(30, win_width - 30), -40, 80, 50, randint(1, 7))
    asteroids.add(asteroid)

monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)

bullets = sprite.Group()

'''игровой цикл'''
finish = False
run = True  # флаг игры, сбрасывается закрытием окна

rel_time = False  # флаг перезарядки
num_fire = 0  # счётчик выстрелов

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                '''проверяем количество выстрелов и не идёт ли перезарядка'''
                if num_fire < 5 and rel_time == False:
                    num_fire += 1
                    fire_sound.play()
                    ship.fire()
                if num_fire >= 5     and rel_time == False:
                    last_time = timer()
                    rel_time = True

    if not finish:
        '''обновляем фон'''
        window.blit(background, (0, 0))

        '''движения спрайтов'''
        ship.update()
        monsters.update()
        bullets.update()
        asteroids.update()

        '''обновляем движения спрайтов'''
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)
        asteroids.draw(window)

        '''перезарядка'''
        if rel_time == True:
            now_time = timer()
            if now_time - last_time < 3:
                reload = font2.render('Перезарядка...', 1, (150, 0, 0))
                window.blit(reload, (260, 460))
            else:
                num_fire = 0  # обнуляем счётчик пуль
                rel_time = False  # сбрасываем флаг перезарядки

        '''проверка столкновения пули и монстра'''
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score += 1
            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)

        '''если спрайт коснулся врага, уменьшается жизнь'''
        if sprite.spritecollide(ship, monsters, False) or sprite.spritecollide(ship, asteroids, False):
            sprite.spritecollide(ship, monsters, True)
            sprite.spritecollide(ship, asteroids, True)
            life -= 1

        '''поражение'''
        if life == 0 or lost >= max_lost:
            finish = True  # проиграли, больше не управляем спрайтами
            window.blit(lose, (200, 200))

        '''победа'''
        if score >= goal:
            finish = True
            window.blit(win, (200, 200))

        '''пишем текст на экране'''
        text = font2.render('Счёт:' + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        text_lose = font2.render('Пропущено:' + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))

        '''задаём разный цвет в зависимости от кол-ва жизней'''
        if life == 3:
            life_color = (0, 150, 0)
        if life == 2:
            life_color = (150, 150, 0)
        if life == 1:
            life_color = (150, 0, 0)

        text_life = font1.render(str(life), 1, life_color)
        window.blit(text_life, (600, 10))

        display.update()

    time.delay(50)