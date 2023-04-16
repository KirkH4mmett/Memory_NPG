import pygame
import random
import time
import random


class Mode:

    def __init__(self, goback_button, mode, easy_words, medium_words, hard_words, screen, font, games_scores):
        self.goback = goback_button
        self.mode = mode
        self.easy = easy_words
        self.medium = medium_words
        self.hard = hard_words
        self.difficulty = "łatwy"
        self.word = ""
        self.words = []
        self.screen = screen
        self.pick = False
        self.wait = False
        self.input = False
        self.new_game = True
        self.game_over = False
        self.font = font
        self.score = 0
        self.guess = ""
        self.games_scores = games_scores
        self.game_count = 1
        self.bg = pygame.image.load("background.jpg")
        self.i = 0
        self.j = 0
        self.komunikat = ""

    def pick_word(self):
        if self.difficulty == "łatwy":
            self.word = random.choice(self.easy)
        elif self.difficulty == "średni":
            self.word = random.choice(self.medium)
        elif self.difficulty == "trudny":
            self.word = random.choice(self.hard)

        self.words.append(self.word)

    def show_word(self, i):
        word_txt = self.font.render(self.words[i], True, (255, 255, 255))
        self.screen.blit(word_txt, (490, 70))

    def show_word_rand(self, i):
        word_txt = self.font.render(self.words[i], True, (255, 255, 255))
        self.screen.blit(word_txt, (random.randint(1, 800), random.randint(1, 300)))

    def run_mode1(self):

        if self.wait:
            time.sleep(1.5)
            self.wait = False
            self.input = True

        elif self.pick:
            if self.i == 0:
                time.sleep(1)
                self.pick_word()

            self.show_word(self.i)
            self.i += 1
            time.sleep(1)

            if self.i == len(self.words):
                self.pick = False
                self.wait = True
                self.i = 0

        elif self.input:
            if self.guess == self.words[self.j]:
                self.j += 1
                self.guess = ""

            if self.j == len(self.words):
                self.j = 0
                self.score += 1
                self.komunikat = "Dobrze! Aktualny wynik: " + str(self.score)
                self.input = False
                self.guess = ""
                self.pick = True

            elif self.guess != "":
                self.game_over = True
                self.games_scores.append(("ilość", self.difficulty, self.score))
                self.words = []
                self.guess = ""
                self.j = 0
                self.i = 0
                self.game_count += 1
                self.input = False

        elif self.new_game:
            self.pick = True
            self.new_game = False

        self.draw_board()

    def run_mode2(self):
        if self.wait:
            time.sleep(1)
            self.wait = False
            self.input = True

        elif self.pick:
            if self.i == 0:
                time.sleep(1)
                self.pick_word()

            self.show_word_rand(self.i)
            self.i += 1
            time.sleep(1)

            if self.i == len(self.words):
                self.pick = False
                self.wait = True
                self.i = 0

        elif self.input:
            if self.guess == self.words[self.j]:
                self.j += 1
                self.guess = ""

            if self.j == len(self.words):
                self.j = 0
                self.score += 1
                self.komunikat = "Dobrze! Aktualny wynik: " + str(self.score)
                self.input = False
                self.guess = ""
                self.pick = True

            elif self.guess != "":
                self.game_over = True
                self.games_scores.append(("losowy", self.difficulty, self.score))
                self.words = []
                self.guess = ""
                self.j = 0
                self.i = 0
                self.game_count += 1
                self.input = False

        elif self.new_game:
            self.pick = True
            self.new_game = False

        self.draw_board()

    def run_mode3(self):
        if self.wait:
            time.sleep(1.5)
            self.wait = False
            self.input = True

        elif self.pick:
            if self.i == 0:
                time.sleep(1)
                self.pick_word()

            self.show_word(self.i)
            self.i += 1
            time.sleep(1)

            if self.i == len(self.words):
                self.pick = False
                self.wait = True
                self.i = 0

        elif self.input:
            if self.guess == self.words[self.j]:
                self.j += 1
                self.guess = ""

            if self.j == len(self.words):
                self.j = 0
                self.score += 1
                self.komunikat = "Dobrze! Aktualny wynik: " + str(self.score)
                self.input = False
                self.guess = ""
                self.pick = True

            elif self.guess != "":
                self.game_over = True
                self.games_scores.append(("czas", self.difficulty, self.score))
                self.words = []
                self.guess = ""
                self.j = 0
                self.i = 0
                self.game_count += 1
                self.input = False

        elif self.new_game:
            self.pick = True
            self.new_game = False

        self.draw_board()

    def draw_board(self):
        self.goback.draw()
        if self.game_over:
            self.komunikat = "Źle! Koniec gry! Wynik: " + str(self.score)
        kom_txt = self.font.render(self.komunikat, True, (255, 255, 255))
        self.screen.blit(kom_txt, (70, 200))
        self.komunikat = ""
        if self.goback.button_clicked():
            self.new_game = True