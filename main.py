import pygame
import sys
import time
from button import Button
from mode import Mode

pygame.init()

screen_width = 900
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory słowne")

clock = pygame.time.Clock()

# Kolory
bg = (90, 90, 90)

clicked = False
font = pygame.font.SysFont("Arial", 30)
mode = "menu"

# Szerokość i wysokość przycisków w menu głównym
m_b_w = 350
m_b_h = 35

# Tworzenie obiektów przycisków menu głównego
play = Button((screen_width-m_b_w)/2, 300, m_b_w, m_b_h, "Graj", 25, screen, clicked)
stats = Button((screen_width-m_b_w)/2, 380, m_b_w, m_b_h, "Statystyki", 25, screen, clicked)
quit = Button((screen_width-m_b_w)/2, 460, m_b_w, m_b_h, "Wyjdź", 25, screen, clicked)

menu_buttons = [play, stats, quit]

# Parametry przycisków menu wyboru trybu
gm_b_w = 200
gm_b_h = 100
gm_b_cnt = 3
gm_b_offset = (screen_width - gm_b_cnt * gm_b_w) / (gm_b_cnt+1)
# Tworzenie przycisków menu wyboru trybu
mode1 = Button(gm_b_offset, 250, gm_b_w, gm_b_h, "Tryb gry 1", 30, screen, clicked)
mode2 = Button(2 * gm_b_offset + gm_b_w, 250, gm_b_w, gm_b_h, "Tryb gry 2", 30, screen, clicked)
mode3 = Button(3 * gm_b_offset + 2 * gm_b_w, 250, gm_b_w, gm_b_h, "Tryb gry 3", 30, screen, clicked)
goback = Button(screen_width-30, 10, 20, 20, "<-", 20, screen, clicked)

gamemode_buttons = [goback, mode1, mode2, mode3]

# Wczytanie słów z pliku


def list_clean(lst):
    for i in range(len(lst)):
        lst[i] = lst[i].replace('\n', '')
    return lst


easy_words_file = open("baza_hasel/hasla_latwy.txt")
medium_words_file = open("baza_hasel/hasla_srednie.txt")
hard_words_file = open("baza_hasel/hasla_trudne.txt")

easy_words = list_clean(easy_words_file.readlines())
medium_words = list_clean(medium_words_file.readlines())
hard_words = list_clean(hard_words_file.readlines())

easy_words_file.close()
medium_words_file.close()
hard_words_file.close()

#Statystyki gry
stat = {}
games_scores = []

new_game = True
active = False
user_text = ""
mode_ = Mode(goback, mode, easy_words, medium_words, hard_words, screen, font, stat, games_scores)

# Główna pętla gry
while True:
    # Zmazanie ekranu
    screen.fill(bg)
    if active:
        text_surface = font.render(user_text, True, (255, 255, 255))
        screen.blit(text_surface, (300, 500))

    # Sprawdzanie wydarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit(0)

        # Wpisywanie
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]

                elif event.key == pygame.K_RETURN:
                    mode_.guess = user_text
                    user_text = ""

                else:
                    user_text += event.unicode

    # Ekran menu głównego
    if mode == "menu":
        # Sprawdzanie kliknięć przycisków menu
        if play.button_clicked():
            mode = "play"
        elif quit.button_clicked():
            pygame.quit()
            sys.exit(0)
        elif stats.button_clicked():
            mode = "stats"

        # Rysowanie przycisków
        for button in menu_buttons:
            button.draw()

    # Ekran statystyk
    elif mode == "stats":
        if goback.button_clicked():
            mode = "menu"

        stats_txt = font.render("N a j l e p s z e   w y n i k i :", True, (159, 43, 104))
        text_len = stats_txt.get_width()
        screen.blit(stats_txt, (100, 100))

        goback.draw()

    # Ekran wyboru trybu gry
    elif mode == "play":
        if goback.button_clicked():
            mode = "menu"
        elif mode1.button_clicked():
            mode = "mode1"
            active = True
        elif mode2.button_clicked():
            mode = "mode2"
        elif mode3.button_clicked():
            mode = "mode3"

        for button in gamemode_buttons:
            button.draw()

    # Ekran trybu gry 1
    elif mode == "mode1":
        if goback.button_clicked():
            mode = "play"
            mode_.new_game = True

        mode_.run_mode1()

        goback.draw()

    # Ekran trybu gry 2
    elif mode == "mode2":
        if goback.button_clicked():
            mode = "play"

        mode1_txt = font.render("W tym miejscu umieścimy naszą grę, tryb nr 2", True, (200, 200, 255))
        text_len = mode1_txt.get_width()
        screen.blit(mode1_txt, (100, 300))

        goback.draw()

    # Ekran trybu gry 3
    elif mode == "mode3":
        if goback.button_clicked():
            mode = "play"

        mode1_txt = font.render("W tym miejscu umieścimy naszą grę, tryb nr 3", True, (200, 200, 255))
        text_len = mode1_txt.get_width()
        screen.blit(mode1_txt, (100, 300))

        goback.draw()

    pygame.display.update()
    clock.tick(60)
