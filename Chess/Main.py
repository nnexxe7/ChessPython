import pygame as p

p.init()
WIDTH = HEIGHT = 800
screen = p.display.set_mode((WIDTH, HEIGHT))
SQ_NUMBER = 8
SQ_SIZE = WIDTH / SQ_NUMBER
clock = p.time.Clock()
running = True
p.display.set_caption('Chess')


def draw_board():
    for row in range(SQ_NUMBER):
        for col in range(SQ_NUMBER):
            if (row + col) % 2 == 0:
                p.draw.rect(screen, (119, 153, 84), p.Rect(row * SQ_SIZE, col * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            else:
                p.draw.rect(screen, (233, 237, 204), p.Rect(row * SQ_SIZE, col * SQ_SIZE, SQ_SIZE, SQ_SIZE))


while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
    draw_board()
    p.display.flip()
    clock.tick(15)
p.quit()
