#Создай собственный Шутер!
from pygame import *
from random import randint

"""Main window"""
print("Выберите режим игры:")
print("Kuplinov")
print("Student")
print("UFO")
print("Anime")
answer = input("").lower()

win_width = 700
win_height = 500

title1 = "ULTA"
title2 = "Спасение от училки"
title3 = "Космическая баталия"
title4 = "Магическая битва."
changetitle = ""
if answer == "kuplinov":
    changetitle = title1
if answer == "student":
    changetitle = title2
if answer == "ufo":
    changetitle = title3
if answer == "anime":
    changetitle = title4
display.set_caption(changetitle)
window = display.set_mode((win_width, win_height))

bg1 = "kuplinovbg.png"
bg2 = "teacher.jpg"
bg3 = "galaxy.jpg"
bg4 = "MGbg.jpg"
changebg = ""
if answer == "kuplinov":
    changebg = bg1
if answer == "student":
    changebg = bg2
if answer == "ufo":
    changebg = bg3
if answer == "anime":
    changebg = bg4
background = transform.scale(image.load(changebg), (win_width, win_height))

"""Music."""
music1 = "Dr.Mixxer_feat._Kuplinov_-_Ulta_.mp3"
music2 = "fonk.mp3"
music3 = "space.mp3"
music4 = "MGmusic.mp3"

changemusic = ""

if answer == "kuplinov":
    changemusic = music1
if answer == "student":
    changemusic = music2
if answer == "ufo":
    changemusic = music3
if answer == "anime":
    changemusic = music4
mixer.init()
mixer.music.load(changemusic)
mixer.music.play()

fire1 = "Pew.mp3"
fire2 = "write.mp3"
fire3 = "fire.ogg"
fire4 = "throw.mp3"
fire_s = ""
if answer == "kuplinov":
    fire_s = fire1
if answer == "student":
    fire_s = fire2
if answer == "ufo":
    fire_s = fire3
if answer == "anime":
    fire_s = fire4
fire_sound = mixer.Sound(fire_s)

""" Шрифты."""
font.init()
font1 = font.SysFont('Arial', 80)
font2 = font.SysFont('Arial', 36)
win = font1.render("   Победа", True, (0, 0, 0))
lose = font1.render("Поражение", True, (0, 0, 0))

lost = 0 # Корааблей пропущено.
score = 0 # Кораблей сбито.
max_lost = 5 # Проиграли, если пропустили какое-то кол-во кораблей.
goal = 100 # Столько кораблей надо сбить.

class GameSprite(sprite.Sprite):
    """Родительский клсс."""

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
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

    def fire(self):
        bullet1 = "like.png"
        bullet2 = "a.png"
        bullet3 = "bullet.png"
        bullet4 = "finger.png"
        changebullet = ""
        bul1 = 15
        bul2 = 20
        if answer == "kuplinov":
            changebullet = bullet1
            bul1 = 40
            bul2 = 40
        if answer == "student":
            changebullet = bullet2
        if answer == "ufo":
            changebullet = bullet3
        if answer == "anime":
            changebullet = bullet4
            bul1 = 30
            bul2 = 50
        bullet = Bullet(changebullet, self.rect.centerx, self.rect.top, bul1, bul2, -15)
        bullets.add(bullet)


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost += 1


class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


"""Sprites"""
ship1 = "KuplinovPlay.png"
ship2 = "student.png"
ship3 = "rocket.png"
ship4 = "Itadori.png"
changeship = ""
cord = 0

if answer == "kuplinov":
    changeship = ship1
    cord = 150
if answer == "student":
    changeship = ship2
    cord = 50
if answer == "ufo":
    changeship = ship3
    cord = 80
if answer == "anime":
    cord = 100
    changeship = ship4
ship = Player(changeship, 5, win_height - 100, cord, 100, 20)
monsters = sprite.Group()

monster1 = "dislike.png"
monster2 = "book.png"
monster3 = "ufo.png"
monster4 = "Sukun.png"
changemonster = ""
cordx = 50
if answer == "kuplinov":
    changemonster = monster1
if answer == "student":
    changemonster = monster2
if answer == "ufo":
    changemonster = monster3
if answer == "anime":
    changemonster = monster4
    cordx = 150
for i in range(1, 6):
    monster = Enemy(changemonster, randint(20, win_width - 80), -40, 80, cordx, randint(3, 5))
    monsters.add(monster)

bullets = sprite.Group()
finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                ship.fire()

    if not finish:
        window.blit(background, (0, 0))
        text = font2.render("Счёт: " + str(score), 1, (0, 0, 0))
        text_lose = font2.render("Пропущено: " + str(lost), 1, (0, 0, 0))
        window.blit(text, (10, 20))
        window.blit(text_lose, (10, 50))
        ship.reset()
        ship.update()
        monsters.update()
        bullets.update()
        bullets.draw(window)
        monsters.draw(window)
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score += 1
            monster = Enemy(changemonster, randint(20, win_width - 80), -40, 80, cordx, randint(3, 5))
            monsters.add(monster)

        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True
            window.blit(lose, (200, 200))

        if score >= goal:
            finish = True
            window.blit(win, (200, 200))
        display.update()
    time.delay(60)


"""
def f3():
    '''область всех закрывающих функций '''

    def f4():
        '''локальная'''
        global number
        number = 10
        print(number)

    global number
    number = 30
    f4()
    print(number)


number = 100
f3()
print(number)


1) Локальная - local scope. Самая внутренняя область (в текущей функции)
2) Encloding - область всех закрывающих функций 
3) Global - глобальная область
"""
