import pygame
import os
import math
import random

pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Logo Quiz")

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 +((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('maturamtscriptcapitals', 70)

raw_sprite = pygame.image.load('sprite.png')
raw_mclaren = pygame.image.load('mclaren.png')
raw_pizzahut = pygame.image.load('pizzahut.png')
raw_msi = pygame.image.load('msi.jpeg')

sprite = pygame.transform.scale(raw_sprite, (200, 200))
mclaren = pygame.transform.scale(raw_mclaren, (200, 200))
pizzahut = pygame.transform.scale(raw_pizzahut, (200, 200))
msi = pygame.transform.scale(raw_msi, (200, 200))

imag = [sprite, mclaren, pizzahut, msi]
images = random.choice(imag)

if images == sprite:
    word = 'SPRITE'
elif images == mclaren:
    word = 'MCLAREN'
elif images == pizzahut:
    word = 'PIZZA HUT'
elif images == msi:
    word = 'MSI'
else:
    pass
guessed = []

WHITE = (255,255,0)
BLACK = (0, 0, 0)

guesscount = 0
FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
    win.fill((WHITE))

    text = TITLE_FONT.render("Logo Quiz", 1, BLACK)
    win.blit(text,(WIDTH/2 - text.get_width()/2, 20))

    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text,(400, 200))

    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images, (150, 100))
    pygame.display.update()

def display_messsage(message):
    pygame.time.delay(2000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)


while run:
    clock.tick(FPS)

    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            guesscount += 1
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)

    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    if won:
        display_messsage("YOU WON!")
        break

    if guesscount == 10 and letter not in guessed:
        display_messsage("YOU LOSE:(")
        break

pygame.quit()
