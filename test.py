import os
import pygame

os.environ["SDL_VIDEO_CENTERED"] = "1"

WIDTH = 900
HEIGHT = 900

#componentes do jogo
btnJogar = Rect((275, 480), (350,70))
btnSom = Rect((275, 580), (350,70))
btnSomJogo = Rect((15, 855), (130,30))
btnRestart = Rect((275, 560), (350,70))

#Actors
ct = Actor("ct", (780, 820)) #principal personagem do jogo

trs = [
    Actor("tr0", (200, 500)), #0
    Actor("tr", (350, 250)), #1
    Actor("tr", (400, 90)), #2
    Actor("tr", (720, 180)), #3
    Actor("tr", (765, 440)) #4
]

for tr in trs:
        tr.estado = "vivo"

shootsct = []
shootstr = []

#Obstaculos
obstaculos = [
    Actor("obstacle00", (284, 476)),
    Actor("obstacle01", (415, 220)),
    Actor("obstacle02", (791.5, 306.5)),
    Actor("obstacle03", (855, 423)),
    Actor("obstacle04", (813.5, 556.5)),
    Actor("obstacle05", (866.5, 645)),
    Actor("obstacle06", (370.5, 741.5)),
    Actor("obstacle07", (336.5, 772.5))
]

#estados iniciais do jogo
estado = "menu"
som = True
delay_shoottr = 50
kills = 4


#funções do jogo
def draw():
    if estado == "menu":
        menu()
    elif estado == "jogo":
        jogo()
    elif estado == "win":
        win()

def update():
    global estado

    if estado == "jogo":
        moverCT()
        limiteTela()
        moverTR()
        shootTR()
        movershootTR()
        movershootCT()
        colisaoShootTrObstacle()
        colisaoShootCtObstacle()
        colisaoShootCtInTr()


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
    global estado, kills

    screen.blit("miragemap", (0, 0))

    for shootct in shootsct:
            shootct.draw()

    ct.draw()

    for shoottr in shootstr:
        shoottr.draw()

    
    for tr in trs:
        if tr.estado == "vivo":
            tr.draw()
        elif tr.estado == "morto":
            kills += 1

    if kills == 5:
        estado = "win"

    for obstaculo in obstaculos:
        obstaculo.draw()

    screen.draw.filled_rect(btnSomJogo, "black")
    
    if som:
        screen.draw.text("Som: ON", center=btnSomJogo.center, color="white", fontsize=25)
    else:
        screen.draw.text("Som: OFF", center=btnSomJogo.center, color="white", fontsize=25)


def win():
    screen.blit("menubg", (0, 0))
    screen.draw.text("Round Win", center = (450, 400), color="green", fontsize= 70)

    screen.draw.filled_rect(btnRestart, "black")
    screen.draw.text("Próximo Round", center=btnRestart.center, color="white", fontsize=50)


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


def on_key_down(key):
    if estado == "jogo" and key == keys.SPACE:
        shootct = Actor("shootct", (ct.x, ct.y))
        shootsct.append(shootct)
        if som == True:
            sounds.m4a4.set_volume(0.1)
            sounds.m4a4.play()
    

def movershootCT():
    for shootct in shootsct:
        shootct.y -=10


def shootTR():
    global delay_shoottr

    if delay_shoottr == 50:
        for i, tr in enumerate(trs):
            if tr.estado == "vivo":
                shoottr = Actor("shoottr", (tr.x, tr.y))
                if i == 0:
                    shoottr.angle = 90

                shootstr.append(shoottr)
    elif delay_shoottr == 0:
        delay_shoottr = 51

    delay_shoottr -= 1

def movershootTR():
    for shoottr in shootstr:
        if shoottr.angle == 90:
            shoottr.x += 10
        else:
            shoottr.y +=10
    
#Colisões
def colisaoObstaculo():
    for obstaculo in obstaculos:
        if ct.colliderect(obstaculo):
            return True
    return False

def colisaoShootTrObstacle():
    for shoottr in shootstr:
        for obstaculo in obstaculos:
            if shoottr.colliderect(obstaculo):
                shootstr.remove(shoottr)
                
def colisaoShootCtObstacle():
    for shootct in shootsct:
        for obstaculo in obstaculos:
            if shootct.colliderect(obstaculo):
                shootsct.remove(shootct)

def colisaoShootCtInTr():
    for shootct in shootsct:
        for tr in trs:
            if tr.estado == "vivo" and shootct.colliderect(tr):
                tr.estado = "morto"
                shootsct.remove(shootct)

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

    if estado == "jogo":
        if btnSomJogo.collidepoint(pos) and som == True:
            som = False
        elif btnSomJogo.collidepoint(pos) and som == False:
            som = True 

    if estado == "win":
        if btnRestart.collidepoint(pos):
            estado = "jogo"


            

