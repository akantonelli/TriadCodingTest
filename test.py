import os

os.environ["SDL_VIDEO_CENTERED"] = "1"

WIDTH = 900
HEIGHT = 900

#estado inicial do jogo
estado = "menu"

def draw():
    if estado == "menu":
        menu()


def menu():
    screen.blit("menubg", (0, 0))

