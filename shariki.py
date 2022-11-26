import pygame
from pygame.draw import *
from random import randint
pygame.init()
u = 700
v = 700
FPS = 30
screen = pygame.display.set_mode((u, v))

font = pygame.font.SysFont('arial', 20)


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
Ex = []
Ey = []
ER = []
col = []
Espeedx = []
Espeedy = []
scope = 0
t = 5

trash = 0

def render(x, y, R, color):
    for i in range(len(x)):
        circle(screen, color[i], (x[i], y[i]), R[i])


def move(dt, vx, vy, x, y, R, u, v):
    for i in range(len(x)):
        if (u-x[i]) < R[i]:
            x[i] = u-R[i]
            vx[i] = -vx[i]
            x[i] += vx[i] * t
        if (v-y[i]) < R[i]:
            vy[i] = -vy[i]
            y[i] += vy[i] * t
            y[i] = v-R[i]
        if y[i] < R[i]:
            vy[i] = -vy[i]
            y[i] += vy[i] * t
            y[i] = R[i]
        if x[i] < R[i]:
            vx[i] = -vx[i]
            x[i] += vx[i] * t
            x[i] = R[i]


        else:
            x[i] += vx[i]*t
            y[i] += vy[i]*t


def remember():
    x = randint(100, 1100)
    y = randint(100, 900)
    R = randint(10, 100)
    color = COLORS[randint(0, 5)]
    Ex.append(x)
    Ey.append(y)
    ER.append(R)
    col.append(color)
    vx = randint(-5, 5)
    vy = randint(-5, 5)
    Espeedx.append(vx)
    Espeedy.append(vy)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

#pygame.mixer.init()

#pygame.event.wait()

wait_time = 1
frame_counter = 0
while not finished:
    clock.tick(FPS)
    screen.fill((0, 0, 0))

    if frame_counter % (FPS * wait_time) == 0:
        if len(Ex) < 10:
            remember()

    render(Ex, Ey, ER, col)
    move(t, Espeedx, Espeedy, Ex, Ey, ER, u, v)
    text = font.render("Score: " + str(scope), True, RED)
    

    # Вывести сделанную картинку на экран в точке (250, 250)
    screen.blit(text, [1, 1])

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(Ex)):
                if (Ex[i] - event.pos[0]) ** 2 + (Ey[i] - event.pos[1]) ** 2 <= ER[i]**2:
                    Ex.pop(i)
                    Ey.pop(i)
                    ER.pop(i)
                    col.pop(i)
                    Espeedy.pop(i)
                    Espeedx.pop(i)
                    scope += 2
                    break

    frame_counter += 1



pygame.quit()

