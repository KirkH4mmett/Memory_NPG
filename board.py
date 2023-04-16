import pygame


class Board:
    def __init__(self):
        pass

    self.draw_board()

    if self.wait:
        time.sleep(1.5)
        self.wait = False
        self.input = True

    elif self.pick:
        if self.i == 0:
            self.pick_word()
        if self.i == len(self.words):
            self.pick = False
            self.wait = True
            self.i = 0
        else:
            self.show_word(self.i)
            self.i += 1
            time.sleep(1)

    elif self.input:
        if self.guess == self.word:
            self.score += 1
            print("Dobrze!")
            self.input = False
            self.guess = ""
            time.sleep(1)
            self.pick = True

        elif self.guess != "":
            print("Koniec Gry!!")
            self.games_scores.append(self.score)
            x = 1
            for sc in self.games_scores:
                print('wynik', x, ':', sc)
                x += 1
            self.score = 0
            self.words = []
            self.guess = ""
            self.game_count += 1
            self.input = False

    elif self.new_game:
        self.pick = True
        self.new_game = False