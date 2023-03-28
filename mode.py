import pygame
import random
import time


class Mode:
    # Kolory
    card_col = (3, 50, 240)
    hover_col = (180, 220, 90)
    text_col = (0, 0, 0)

    def __init__(self, goback_button, mode, easy_words, medium_words, hard_words, screen, font):
        self.goback = goback_button
        self.mode = mode
        self.easy = easy_words
        self.medium = medium_words
        self.hard = hard_words
        self.word = ""
        self.screen = screen
        self.pick = False
        self.wait = False
        self.input = False
        self.new_game = True
        self.font = font
        self.score = 0
        self.guess = ""

    def pick_word(self):
        self.word = random.choice(self.easy)

    def show_word(self):
        word_txt = self.font.render(self.word, True, (200, 200, 200))
        # text_len = word_txt.get_width()
        self.screen.blit(word_txt, (200, 300))

    def run_mode1(self):
        self.draw_board()

        if self.wait:
            time.sleep(2)
            self.wait = False
            self.input = True

        elif self.pick:
            self.pick_word()
            self.pick = False
            self.wait = True
            self.show_word()

        elif self.input:
            if self.guess == self.word:
                self.score += 1
                print("Wynik to: ", self.score)
                time.sleep(2)
                self.pick = True
                self.input = False
                self.guess = ""

            elif self.guess != "":
                print("Koniec Gry!!")
                print("Twój wynik to: ", self.score)
                self.score = 0
                self.input = False

        elif self.new_game:
            self.pick = True
            self.new_game = False

    def run_mode2(self):
        self.draw_board()

    def run_mode3(self):
        self.draw_board()

    def draw_board(self):
        self.goback.draw()
        if self.goback.button_clicked():
            self.new_game = True
            print("nowa gra")
