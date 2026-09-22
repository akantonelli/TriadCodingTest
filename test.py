import os
import pygame

os.environ["SDL_VIDEO_CENTERED"] = "1"

WIDTH = 900
HEIGHT = 900

#componentes do jogo
btnJogar = Rect((275, 480), (350,70))
btnSom = Rect((275, 580), (350,70))

#Actors
ct = Actor("ct", (755, 800)) #principal personagem do jogo

trs = [
    Actor("tr", (720, 200)),
    Actor("tr", (750, 440)),
    Actor("tr", (400, 110)),
    Actor("tr", (320, 250)),
    Actor("tr0", (200, 500))
]

#Obstaculos
obstaculos = [
    Actor("obstaclemap00"),
    Actor("obstaclemap01"),
    Actor("obstaclewall")
]

#estados iniciais do jogo
estado = "menu"
som = True


#funções do jogo
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

    ct.draw()

    for tr in trs:
        tr.draw()

    for obstaculo in obstaculos:
        obstaculo.draw()


#Função para movimentar o personagem
def moverCT():
        
    if keyboard.left:
        ct.x -= 2         
    if keyboard.right:
        ct.x += 2
    if keyboard.up:
        ct.y -= 2
    if keyboard.down:
        ct.y += 2

def limiteTela():
    if ct.x < 0:
        ct.x = 0
    if ct.x > WIDTH:
        ct.x = WIDTH
    if ct.y < 0:
        ct.y = 0
    if ct.y > HEIGHT:
        ct.y = HEIGHT


def update():
    global estado

    if estado == "jogo":
        moverCT()
        limiteTela()


def on_mouse_down(pos):
    global estado, som

    if estado == "menu":
        if btnJogar.collidepoint(pos):
            estado = "jogo"


        if btnSom.collidepoint(pos) and som == True:
            som = False
        elif btnSom.collidepoint(pos) and som == False:
            som = True            
        
            

