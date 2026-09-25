import os
import pygame

os.environ["SDL_VIDEO_CENTERED"] = "1"

WIDTH = 900
HEIGHT = 900

#componentes do jogo
btnJogar = Rect((275, 480), (350,70))
btnSom = Rect((275, 580), (350,70))

#Actors
ct = Actor("ct", (780, 820)) #principal personagem do jogo

trs = [
    Actor("tr0", (200, 500)), #0
    Actor("tr", (350, 250)), #1
    Actor("tr", (400, 90)), #2
    Actor("tr", (720, 180)), #3
    Actor("tr", (765, 440)) #4
]

shootsct = []
shootstr = []

#Obstaculos
obstaculos = [
    Actor("obstacle00", (284, 476)),
    Actor("obstacle01", (415, 220)),
    #Actor("obstaclewall")
]

#estados iniciais do jogo
estado = "menu"
som = True
delay_shoottr = 50


#funções do jogo
def draw():
    if estado == "menu":
        menu()
    elif estado == "jogo":
        jogo()

def update():
    global estado

    if estado == "jogo":
        moverCT()
        limiteTela()
        moverTR()
        shootCT()
        shootTR()


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

    for shootct in shootsct:
            shootct.draw()

    ct.draw()

    for shoottr in shootstr:
        shoottr.draw()

    for tr in trs:
        tr.draw()

    for obstaculo in obstaculos:
        obstaculo.draw()

    


#Função para movimentar o personagem
def moverCT():
       
    if keyboard.left:
        ct.x -= 2
        if colisaoObstaculo():
            ct.x += 2      
    if keyboard.right:
        ct.x += 2
        if colisaoObstaculo():
            ct.x -= 2
    if keyboard.up:
        ct.y -= 2
        if colisaoObstaculo():
            ct.y += 2
    if keyboard.down:
        ct.y += 2
        if colisaoObstaculo():
            ct.y -= 2


direcaoTR0 = "desce"
direcaoTR2 = "direita"
direcaoTR3 = "esquerda"
direcaoTR4 = "esquerda"
def moverTR():
    global direcaoTR0, direcaoTR2, direcaoTR3, direcaoTR4

    #0
    if direcaoTR0 == "desce":
        trs[0].y += 2
        if trs[0].y >= 650:
            direcaoTR0 = "sobe"
    elif direcaoTR0 == "sobe":
        trs[0].y -= 2
        if trs[0].y <= 460:
            direcaoTR0 = "desce"

    #2
    if direcaoTR2 == "direita":
        trs[2].x += 1.8
        if trs[2].x >= 530:
            direcaoTR2 = "esquerda"
    elif direcaoTR2 == "esquerda":
        trs[2].x -= 2
        if trs[2].x <= 430:
            direcaoTR2 = "direita"

    #3
    if direcaoTR3 == "esquerda":
        trs[3].x -= 1.5
        if trs[3].x <= 620:
            direcaoTR3 = "direita"
    elif direcaoTR3 == "direita":
        trs[3].x += 2.5
        if trs[3].x >= 720:
            direcaoTR3 = "esquerda"

    #4
    if direcaoTR4 == "esquerda":
        trs[4].x -= 1.5
        if trs[4].x <= 700:
            direcaoTR4 = "direita"
    elif direcaoTR4 == "direita":
        trs[4].x += 1.5
        if trs[4].x >= 765:
            direcaoTR4 = "esquerda"


def shootCT():
    if keyboard.space:
        shootct = Actor("shootct", (ct.x, ct.y))
        shootsct.append(shootct)

def shootTR():
    global delay_shoottr

    if delay_shoottr == 50:
        for i, tr in enumerate(trs):
            shoottr = Actor("shoottr", (tr.x, tr.y))
            if i == 0:
                shoottr.angle = 90
            shootstr.append(shoottr)
    elif delay_shoottr == 0:
        delay_shoottr = 51

    delay_shoottr -= 1
    
def colisaoObstaculo():
    for obstaculo in obstaculos:
        if ct.colliderect(obstaculo):
            return True
    return False


def limiteTela():
    if ct.x < 0:
        ct.x = 0
    if ct.x > WIDTH:
        ct.x = WIDTH
    if ct.y < 0:
        ct.y = 0
    if ct.y > HEIGHT:
        ct.y = HEIGHT


def on_mouse_down(pos):
    global estado, som

    if estado == "menu":
        if btnJogar.collidepoint(pos):
            estado = "jogo"


        if btnSom.collidepoint(pos) and som == True:
            som = False
        elif btnSom.collidepoint(pos) and som == False:
            som = True            
        
            

