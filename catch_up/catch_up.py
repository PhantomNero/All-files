from pygame import *

# Создай окно игры.
window = display.set_mode((720, 500))
display.set_caption("catch-up")

# Задай фон сцены.
background = transform.scale(image.load("Minecraft.png"), (720, 500))
# Создай 2 спрайта и размести их на сцене.
x1 = 100
y1 = 260

x2 = 500
y2 = 260

sprite1 = transform.scale(image.load('pngegg (1).png'), (100, 100))
sprite2 = transform.scale(image.load('pngegg.png'), (100, 100))


# Обработай событие «клик по кнопке "Закрыть окно"».
speed = 5
run = True  # Флаг.
clock = time.Clock()
while run:
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    for i in event.get():
        if i.type == QUIT:
            run = False
    keys_pressed = key.get_pressed()

    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 395:
        y1 += speed


    if keys_pressed[K_a] and x2 > 5:
        x2 -= speed
    if keys_pressed[K_d] and x2 < 595:
        x2 += speed
    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed
    if keys_pressed[K_s] and y2 < 395:
        y2 += speed

    display.update()