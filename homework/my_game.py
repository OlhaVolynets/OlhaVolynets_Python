# Написати код анімації квадрата, який переміщається від лівої межі до правої,
# дотикається до неї, але не зникає за нею.
# Після цього повертається назад – від правої межі до лівої, дотикається до неї,
# і знову рухається вправо. Цикли руху квадрата повторюються до завершення програми.

import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("my first game")

x = 0
y = 0
width = 50
height = 50
vol = 10

run = True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if x == 0:
        road = "right"
    elif x == 460:
        road = "left"
    if road == "right":
        x += vol
    else:
        x -= vol

    screen.fill((128, 128, 128))
    pygame.draw.rect(screen, (255, 255, 0), (x, y, width, height))
    pygame.display.update()


pygame.quit()
