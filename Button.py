import pygame
from pygame import Surface, Rect


class Button:
    identifier: str
    pos: tuple
    dimensions: tuple

    def __init__(self, identifier: str, pos: tuple, dimensions: tuple, command=None, text=None, font=None):
        self.identifier = identifier
        self.rect = Rect(pos, dimensions)
        self.command = command
        self.text = text
        self.font = font

    def execute(self):
        """executes self.command()"""
        self.command()

    def render_text(self) -> (Surface, Rect):
        """returns a rendered text with proper font in black colour and
        a rectangle in which the rendered text will be placed in"""
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        return text_surface, text_surface.get_rect()

    def draw_text(self, display: Surface):
        """draws rendered text in the center of rectangle"""
        text_surf, text_rect = self.render_text()
        center_x = (self.rect.left + (self.rect.width / 2))
        center_y = (self.rect.top + (self.rect.height / 2))
        text_rect.center = (center_x, center_y)
        display.blit(text_surf, text_rect)

    def draw_state(self, display: Surface, state: str):
        """draws rectangle with a colour depending on the given state"""
        if state == 'regular':
            pygame.draw.rect(display, (100, 100, 255), self.rect)
        elif state == 'within':
            pygame.draw.rect(display, (0, 0, 200), self.rect)
        elif state == 'clicking':
            pygame.draw.rect(display, (100, 100, 255), self.rect)

    def is_within(self, mouse_pos: tuple) -> bool:
        """returns true if mouse is inside rectangle; false otherwise"""
        return self.rect.collidepoint(mouse_pos[0], mouse_pos[1])

    def draw_button(self, display: Surface, mouse_pos: tuple, clicking: bool):
        """execute draw_text on display if text exists and draw_state on display
        with state given by:
        is_within and clicking     -> 'clicking'
        is_within and not clicking -> 'within'
        not is_within              -> 'regular'"""
        if self.is_within(mouse_pos):
            if clicking:
                self.draw_state(display, 'clicking')
            else:
                self.draw_state(display, 'within')
        else:
            self.draw_state(display, 'regular')

        if (self.text is not None) and (self.font is not None):
            self.draw_text(display)
