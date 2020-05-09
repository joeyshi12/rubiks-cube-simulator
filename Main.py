import sys
import pygame
from pygame.locals import *
from RubiksCube import RubiksCube
from Button import Button

pygame.init()
pygame.display.set_caption('Rubik\'s Cube Simulator')
fps = 60
fpsClock = pygame.time.Clock()
width, height = 680, 440
screen = pygame.display.set_mode((width, height))

FRONT_TOP_LEFT = (220, 160)
PADDING = 40
LENGTH = 32
BUTTON_WIDTH = 80
BUTTON_HEIGHT = 32
rc = RubiksCube()
state = [False, False]
font = pygame.font.SysFont('lucidaconsole', 14)


def draw_face(screen, face_idx, start_pos):
    face = rc.faces[face_idx]
    x, y = start_pos
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, rc.COLOUR_MAP[face[i][j]], (x, y, LENGTH, LENGTH))
            x += PADDING
        x = start_pos[0]
        y += PADDING


def draw_cube(screen):
    draw_face(screen, 0, FRONT_TOP_LEFT)
    draw_face(screen, 1, (FRONT_TOP_LEFT[0] - 3 * PADDING, FRONT_TOP_LEFT[1]))
    draw_face(screen, 2, (FRONT_TOP_LEFT[0], FRONT_TOP_LEFT[1] - 3 * PADDING))
    draw_face(screen, 3, (FRONT_TOP_LEFT[0], FRONT_TOP_LEFT[1] + 3 * PADDING))
    draw_face(screen, 4, (FRONT_TOP_LEFT[0] + 3 * PADDING, FRONT_TOP_LEFT[1]))
    draw_face(screen, 5, (FRONT_TOP_LEFT[0] + 6 * PADDING, FRONT_TOP_LEFT[1]))


def key_handle(key):
    if key == pygame.K_n:
        state[1] = not state[1]
    if key == pygame.K_RIGHT:
        if state[1]:
            rc.right()
        else:
            rc.right_prime()
    if key == pygame.K_UP:
        if state[1]:
            rc.up()
        else:
            rc.up_prime()
    if key == pygame.K_LEFT:
        if state[1]:
            rc.left()
        else:
            rc.left_prime()
    if key == pygame.K_DOWN:
        if state[1]:
            rc.down()
        else:
            rc.down_prime()
    if key == pygame.K_SPACE:
        if state[1]:
            rc.front()
        else:
            rc.front_prime()
    if key == pygame.K_b:
        if state[1]:
            rc.back()
        else:
            rc.back_prime()


def start_reset():
    if rc.is_solved():
        return
    else:
        state[0] = True


def mode():
    if state[1]:
        return 'Counter Clockwise'
    else:
        return 'Clockwise'


def main():
    reset_button_x = FRONT_TOP_LEFT[0] + LENGTH + 8 * PADDING - BUTTON_WIDTH
    reset_button_y = FRONT_TOP_LEFT[1] + LENGTH + 4 * PADDING - BUTTON_HEIGHT
    reset_button = Button('reset', (reset_button_x, reset_button_y), (BUTTON_WIDTH, BUTTON_HEIGHT), start_reset,
                          'Reset', font)

    shuffle_button_x = FRONT_TOP_LEFT[0] + LENGTH + 8 * PADDING - BUTTON_WIDTH
    shuffle_button_y = FRONT_TOP_LEFT[1] + LENGTH + 5 * PADDING - BUTTON_HEIGHT
    shuffle_button = Button('shuffle', (shuffle_button_x, shuffle_button_y), (BUTTON_WIDTH, BUTTON_HEIGHT), rc.shuffle,
                            'Shuffle', font)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                key_handle(event.key)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset_button.is_within(pygame.mouse.get_pos()):
                    reset_button.execute()
                if shuffle_button.is_within(pygame.mouse.get_pos()):
                    shuffle_button.execute()
        screen.fill((0, 0, 0))

        if state[0]:
            rc.step_back()
            if rc.is_solved():
                state[0] = False

        mode_render = font.render("Mode: " + mode(), True, (255, 255, 255))
        screen.blit(mode_render, (10,10))
        draw_cube(screen)
        reset_button.draw_button(screen, pygame.mouse.get_pos(), pygame.mouse.get_pressed() == (1, 0, 0))
        shuffle_button.draw_button(screen, pygame.mouse.get_pos(), pygame.mouse.get_pressed() == (1, 0, 0))
        pygame.display.flip()
        fpsClock.tick(fps)


if __name__ == '__main__':
    main()
