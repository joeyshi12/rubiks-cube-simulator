import sys
import pygame
from pygame.locals import *
from RubiksCube import RubiksCube
from Button import Button

pygame.init()
pygame.display.set_caption('Rubik\'s Cube Simulator')
fps = 60
fpsClock = pygame.time.Clock()
width, height = 680, 460
screen = pygame.display.set_mode((width, height))

FRONTTOPLEFT = (200, 160)
PADDING = 50
LENGTH = 32
COLOURS = {'W': (255, 255, 255), 'R': (255, 0, 0), 'G': (0, 255, 0), 'B': (0, 0, 255), 'O': (255, 165, 0),
           'Y': (255, 255, 0)}
rc = RubiksCube()


def drawFace(screen, faceIdx, startPos):
    face = rc.faces[faceIdx]
    x, y = startPos
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, COLOURS[face[i][j]], (x, y, LENGTH, LENGTH))
            x += PADDING
        x = startPos[0]
        y += PADDING


def drawCube(screen):
    drawFace(screen, 0, FRONTTOPLEFT)
    drawFace(screen, 1, (FRONTTOPLEFT[0] - 3 * PADDING, FRONTTOPLEFT[1]))
    drawFace(screen, 2, (FRONTTOPLEFT[0], FRONTTOPLEFT[1] - 3 * PADDING))
    drawFace(screen, 3, (FRONTTOPLEFT[0], FRONTTOPLEFT[1] + 3 * PADDING))
    drawFace(screen, 4, (FRONTTOPLEFT[0] + 3 * PADDING, FRONTTOPLEFT[1]))
    drawFace(screen, 5, (FRONTTOPLEFT[0] + 6 * PADDING, FRONTTOPLEFT[1]))


def keyHandle(key):
    if key == pygame.K_RIGHT:
        rc.right()
    if key == pygame.K_UP:
        rc.up()
    if key == pygame.K_LEFT:
        rc.left()
    if key == pygame.K_DOWN:
        rc.down()
    if key == pygame.K_SPACE:
        rc.front()
    if key == pygame.K_b:
        rc.back()


def solveCube():
    print("TO BE CONTINUED")
    return


def main():
    solveButtonX = FRONTTOPLEFT[0] + LENGTH + 8 * PADDING - 100
    solveButtonY = FRONTTOPLEFT[1] + LENGTH + 4 * PADDING - 40
    solveButtonFont = pygame.font.SysFont('lucidaconsole', 12)
    solveButton = Button('solve', (solveButtonX, solveButtonY), (100, 40), rc.shuffle, 'Solve', solveButtonFont)

    shuffleButtonX = FRONTTOPLEFT[0] + LENGTH + 8 * PADDING - 100
    shuffleButtonY = FRONTTOPLEFT[1] + LENGTH + 5 * PADDING - 40
    shuffleButtonFont = pygame.font.SysFont('lucidaconsole', 12)
    shuffleButton = Button('shuffle', (shuffleButtonX, shuffleButtonY), (100, 40), rc.shuffle, 'Shuffle',
                           shuffleButtonFont)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                keyHandle(event.key)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if solveButton.is_within(pygame.mouse.get_pos()):
                    solveCube()
                if shuffleButton.is_within(pygame.mouse.get_pos()):
                    rc.shuffle()
        screen.fill((0, 0, 0))
        drawCube(screen)
        solveButton.draw_button(screen, pygame.mouse.get_pos(), pygame.mouse.get_pressed() == (1, 0, 0))
        shuffleButton.draw_button(screen, pygame.mouse.get_pos(), pygame.mouse.get_pressed() == (1, 0, 0))
        pygame.display.flip()
        fpsClock.tick(fps)


if __name__ == '__main__':
    main()
