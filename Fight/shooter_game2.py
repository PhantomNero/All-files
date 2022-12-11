#Создай собственный Шутер!
from pygame import *
from random import randint


'''создаём окно'''
win_width = 700
win_height = 500
display.set_caption('Космическая баталия')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))


'''фоновая музыка'''
mixer.init()
mixer.music.load('space.mp3')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

'''шрифты и надписи'''
font.init()
font1 = font.Font(None, 80)
win = font1.render('ПОБЕДА', True, (255, 255, 255))
lose = font1.render('ПОРАЖЕНИЕ', True, (180, 0, 0))
font2 = font.Font(None, 36)

score = 0 #сбито кораблей
lost = 5 #пропущено кораблей
max_lost = 3 #проиграли, если пропустили столько кораблей
goal = 30 #столько кораблей нужно сбить для победы


class GameSprite(sprite.Sprite):
    '''класс-родитель для других спрайтов'''
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        '''каждый спрайт хранит изображение'''
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        '''каждый спрайт - прямоугольник rectangle'''
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        '''отрисовка героя на окне'''
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    '''класс главного игрока'''
    def update(self):
        '''метод для управления спрайтом'''
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        '''стрельба'''
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)


class Enemy(GameSprite):
    '''класс спрайта-врага'''
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost += 1


class Bullet(GameSprite):
    '''класс спрайта-пули'''
    def update(self):
        '''движение пули'''
        self.rect.y += self.speed
        '''исчезает, дойдя до края экрана'''
        if self.rect.y < 0:
            self.kill()



'''создаём спрайты'''
ship = Player('rocket.png', 5, win_height - 100, 80, 100, 10)
#player_image, player_x, player_y, size_x, size_y, player_speed

monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)

bullets = sprite.Group()


'''переменная "игра закончилась"'''
finish = False
'''Основной цикл игры:'''
run = True
while run:
    for e in event.get():
        '''нажатие кнопки "закрыть":'''
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                ship.fire()

    if not finish:
        '''обновляем фон'''
        window.blit(background, (0, 0))

        '''пишем текст на экране'''
        text = font2.render('Счёт:' + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        text_lose = font2.render('Пропущено:' + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))

        '''движения спрайтов'''
        ship.update()
        monsters.update()
        bullets.update()
        '''обновляем местоположение спрайтов'''
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)

        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score += 1
            monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)

        '''поражение'''
        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True
            window.blit(lose, (200, 200))


        '''победа'''
        if score >= goal:
            finish = True
            window.blit(win, (200, 200))


        display.update()
    time.delay(50)