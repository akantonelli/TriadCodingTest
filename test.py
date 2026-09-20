import os

os.environ["SDL_VIDEO_CENTERED"] = "1"

WIDTH = 900
HEIGHT = 900

#componentes do jogo
btnJogar = Rect((275, 480), (350,70))
btnSom = Rect((275, 580), (350,70))

#estados iniciais do jogo
estado = "menu"
som = True

def draw():
    if estado == "menu":
        menu()


def menu():
    screen.blit("menubg", (0, 0))

    screen.draw.filled_rect(btnJogar, "black")
    screen.draw.text("Jogar", center=btnJogar.center, color="white", fontsize=50)

    screen.draw.filled_rect(btnSom, "black")

    if som:
        screen.draw.text("Som: ON", center=btnSom.center, color="white", fontsize=50)
    else:
        screen.draw.text("Som: OFF", center=btnSom.center, color="white", fontsize=50)


