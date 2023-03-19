import pygame
from pygame.locals import *


class Button:
    # Kolory
    button_col = (150, 50, 50)
    hover_col = (100, 40, 40)
    click_col = (50, 100, 100)
    text_col = (0, 0, 0)

    # To się wywołuje tylko raz, przy tworzeniu obiektu
    # dopisek self. oznacza, że dla każdego z obiektów te wartości mogą się różnić (w zależności od tego jakie parametry
    # były przekazywane podczas tworzenia obiektu)
    def __init__(self, x, y, width, height, text, font_size, screen, clicked):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.clicked = clicked

        self.text = text
        self.font_size = font_size
        self.font = pygame.font.SysFont("Constantia", self.font_size)
        self.text_img = self.font.render(self.text, True, self.text_col)
        self.text_len = self.text_img.get_width()

        self.pos = (self.x + int(self.width / 2) - int(self.text_len / 2), self.y + (self.height - self.font_size) / 2)

    def button_clicked(self):
        action = False

        pos = pygame.mouse.get_pos()
        button_rect = Rect(self.x, self.y, self.width, self.height)

        # Instrukcja, która zapobiega wielokrotnemu wywołaniu akcji przycisku po jego kliknięciu
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
            elif pygame.mouse.get_pressed()[0] == 0 and self.clicked:
                self.clicked = False
                action = True

        return action

    def button_hovered(self):
        pos = pygame.mouse.get_pos()
        button_rect = Rect(self.x, self.y, self.width, self.height)

        if button_rect.collidepoint(pos):
            return True

        return False

    def draw(self):

        pygame.draw.rect(self.screen, self.hover_col if self.button_hovered() else self.button_col,
                         (self.x, self.y, self.width, self.height))

        self.screen.blit(self.text_img, self.pos)
