import os
import pygame

os.environ["SDL_VIDEO_CENTERED"] = "1"

WIDTH = 900
HEIGHT = 900

#componentes do jogo
btnJogar = Rect((275, 480), (350,70))
btnSom = Rect((275, 580), (350,70))

#Actors
player = Actor("ct", (755, 840)) #principal personagem do jogo

enemies = [
    Actor("tr", (720, 200)),
    Actor("tr", (750, 440)),
    Actor("tr", (400, 110)),
    Actor("tr", (320, 250)),
    Actor("tr0", (200, 500))
]

               
#estados iniciais do jogo
estado = "menu"
som = True

def draw():
    if estado == "menu":
        menu()
    elif estado == "jogo":
        jogo()

def menu():
    screen.blit("menubg", (0, 0))

    screen.draw.filled_rect(btnJogar, "black")
    screen.draw.text("Jogar", center=btnJogar.center, color="white", fontsize=50)

    screen.draw.filled_rect(btnSom, "black")

    if som:
        screen.draw.text("Som: ON", center=btnSom.center, color="white", fontsize=50)
    else:
        screen.draw.text("Som: OFF", center=btnSom.center, color="white", fontsize=50)


def jogo():
    screen.blit("miragemap", (0, 0))

    player.draw()

    for enemy in enemies:
        enemy.draw()

def on_mouse_down(pos):
    global estado, som

    if estado == "menu":
        if btnJogar.collidepoint(pos):
            estado = "jogo"


        if btnSom.collidepoint(pos) and som == True:
            som = False
        elif btnSom.collidepoint(pos) and som == False:
            som = True            
        
            

