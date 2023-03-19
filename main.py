import pygame
import sys
from button import Button

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


# Główna pętla gry
while True:
    # Zmazanie ekranu
    screen.fill(bg)

    # Sprawdzanie wydarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit(0)

    # Ekran menu głównego
    if mode == "menu":
        # Sprawdzanie kliknięć przycisków menu
        if play.button_clicked():
            mode = "play"
        if quit.button_clicked():
            pygame.quit()
            sys.exit(0)
        if stats.button_clicked():
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

        mode1_txt = font.render("W tym miejscu umieścimy naszą grę, tryb nr 1", True, (200, 200, 255))
        text_len = mode1_txt.get_width()
        screen.blit(mode1_txt, (100, 300))

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
