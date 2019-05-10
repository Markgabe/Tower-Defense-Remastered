from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.window import *
from PPlay.sound import *
from Functions import *
import pygame

def criawave():

    inim1w1 = [Sprite("inimigo1.png") for i in range(20)]
    inim2w1 = [Sprite("inimigo2.png") for i in range(10)]
    for i in range(20):
        if i + 1 <= 10:
            inim1w1[i].x = -10 - 30*i
            inim1w1[i].y = 50
            inim2w1[i].x = -10 - 30*i
            inim2w1[i].y = 50
        else:
            inim1w1[i].x = -10 - 30 * i
            inim1w1[i].y = 50

    inim1w2 = [Sprite("inimigo1.png") for i in range(20)]
    inim2w2 = [Sprite("inimigo2.png") for i in range(15)]
    inim3w2 = [Sprite("inimigo3.png") for i in range(10)]
    for i in range(20):
        if i + 1 <= 10:
            inim1w2[i].x = -10 - 30 * i
            inim1w2[i].y = 50
            inim2w2[i].x = -10 - 30 * i
            inim2w2[i].y = 50
            inim3w2[i].x = -10 - 30 * i
            inim3w2[i].y = 50
        elif i + 1 <= 15 and i + 1 > 10:
            inim1w2[i].x = -10 - 30 * i
            inim1w2[i].y = 50
            inim2w2[i].x = -10 - 30 * i
            inim2w2[i].y = 50
        else:
            inim1w2[i].x = -10 - 30 * i
            inim1w2[i].y = 50

    inim1w3 = [Sprite("inimigo1.png") for i in range(30)]
    inim2w3 = [Sprite("inimigo2.png") for i in range(20)]
    inim3w3 = [Sprite("inimigo3.png") for i in range(15)]
    inim4w3 = [Sprite("inimigo4.png") for i in range(10)]
    for i in range(30):
        if i + 1 <= 10:
            inim1w3[i].x = -10 - 30 * i
            inim1w3[i].y = 50
            inim2w3[i].x = -10 - 30 * i
            inim2w3[i].y = 50
            inim3w3[i].x = -10 - 30 * i
            inim3w3[i].y = 50
            inim4w3[i].x = -10 - 30 * i
            inim4w3[i].y = 50
        elif i + 1 <= 15 and i + 1 > 10:
            inim1w3[i].x = -10 - 30 * i
            inim1w3[i].y = 50
            inim2w3[i].x = -10 - 30 * i
            inim2w3[i].y = 50
            inim3w3[i].x = -10 - 30 * i
            inim3w3[i].y = 50
        elif i + 1 <= 20 and i + 1 > 10:
            inim1w3[i].x = -10 - 30 * i
            inim1w3[i].y = 50
            inim2w3[i].x = -10 - 30 * i
            inim2w3[i].y = 50
        else:
            inim1w3[i].x = -10 - 30 * i
            inim1w3[i].y = 50

    inim1w4 = [Sprite("inimigo1.png") for i in range(40)]
    inim2w4 = [Sprite("inimigo2.png") for i in range(30)]
    inim3w4 = [Sprite("inimigo3.png") for i in range(20)]
    inim4w4 = [Sprite("inimigo4.png") for i in range(15)]
    inim5w4 = [Sprite("inimigo5.png") for i in range(10)]
    for i in range(40):
        if i + 1 <= 10:
            inim1w4[i].x = -10 - 30 * i
            inim1w4[i].y = 50
            inim2w4[i].x = -10 - 30 * i
            inim2w4[i].y = 50
            inim3w4[i].x = -10 - 30 * i
            inim3w4[i].y = 50
            inim4w4[i].x = -10 - 30 * i
            inim4w4[i].y = 50
            inim5w4[i].x = -10 - 30 * i
            inim5w4[i].y = 50
        elif i + 1 <= 15 and i + 1 > 10:
            inim1w4[i].x = -10 - 30 * i
            inim1w4[i].y = 50
            inim2w4[i].x = -10 - 30 * i
            inim2w4[i].y = 50
            inim3w4[i].x = -10 - 30 * i
            inim3w4[i].y = 50
            inim4w4[i].x = -10 - 30 * i
            inim4w4[i].y = 50
        elif i + 1 <= 20 and i + 1 > 10:
            inim1w4[i].x = -10 - 30 * i
            inim1w4[i].y = 50
            inim2w4[i].x = -10 - 30 * i
            inim2w4[i].y = 50
            inim3w4[i].x = -10 - 30 * i
            inim3w4[i].y = 50
        elif i + 1 <= 30 and i+ 1 > 10:
            inim1w4[i].x = -10 - 30 * i
            inim1w4[i].y = 50
            inim2w4[i].x = -10 - 30 * i
            inim2w4[i].y = 50
        else:
            inim1w4[i].x = -10 - 30 * i
            inim1w4[i].y = 50

    inim1w5 = [Sprite("inimigo1.png") for i in range(50)]
    inim2w5 = [Sprite("inimigo2.png") for i in range(40)]
    inim3w5 = [Sprite("inimigo3.png") for i in range(30)]
    inim4w5 = [Sprite("inimigo4.png") for i in range(20)]
    inim5w5 = [Sprite("inimigo5.png") for i in range(15)]
    inim6w5 = [Sprite("inimigo6.png") for i in range(10)]
    for i in range(50):
        if i + 1 <= 10:
            inim1w5[i].x = -10 - 30 * i
            inim1w5[i].y = 50
            inim2w5[i].x = -10 - 30 * i
            inim2w5[i].y = 50
            inim3w5[i].x = -10 - 30 * i
            inim3w5[i].y = 50
            inim4w5[i].x = -10 - 30 * i
            inim4w5[i].y = 50
            inim5w5[i].x = -10 - 30 * i
            inim5w5[i].y = 50
            inim6w5[i].x = -10 - 30 * i
            inim6w5[i].y = 50
        elif i + 1 <= 15 and i + 1 > 10:
            inim1w5[i].x = -10 - 30 * i
            inim1w5[i].y = 50
            inim2w5[i].x = -10 - 30 * i
            inim2w5[i].y = 50
            inim3w5[i].x = -10 - 30 * i
            inim3w5[i].y = 50
            inim4w5[i].x = -10 - 30 * i
            inim4w5[i].y = 50
            inim5w5[i].x = -10 - 30 * i
            inim5w5[i].y = 50
        elif i + 1 <= 20 and i + 1 > 10:
            inim1w5[i].x = -10 - 30 * i
            inim1w5[i].y = 50
            inim2w5[i].x = -10 - 30 * i
            inim2w5[i].y = 50
            inim3w5[i].x = -10 - 30 * i
            inim3w5[i].y = 50
            inim4w5[i].x = -10 - 30 * i
            inim4w5[i].y = 50
        elif i + 1 <= 30 and i + 1 > 10:
            inim1w5[i].x = -10 - 30 * i
            inim1w5[i].y = 50
            inim2w5[i].x = -10 - 30 * i
            inim2w5[i].y = 50
            inim3w5[i].x = -10 - 30 * i
            inim3w5[i].y = 50
        elif i + 1 <= 40 and i + 1 > 10:
            inim1w5[i].x = -10 - 30 * i
            inim1w5[i].y = 50
            inim2w5[i].x = -10 - 30 * i
            inim2w5[i].y = 50
        else:
            inim1w5[i].x = -10 - 30 * i
            inim1w5[i].y = 50

    inimigosw1 = [inim1w1, inim2w1]
    inimigosw2 = [inim1w2, inim2w2, inim3w2]
    inimigosw3 = [inim1w3, inim2w3, inim3w3, inim4w3]
    inimigosw4 = [inim1w4, inim2w4, inim3w4, inim4w4, inim5w4]
    inimigosw5 = [inim1w5, inim2w5, inim3w5, inim4w5, inim5w5, inim6w5]

    return inimigosw1, inimigosw2, inimigosw3, inimigosw4, inimigosw5

def movehorda(horda,inimigos):
    if horda == 1:
        for inim in range(len(inimigos)):
            for i in inimigos[inim]:
                i.draw()
                if inim == 0:
                    if timerw1[0] > 3:
                        move(i,dif,1*vel)
                elif inim == 1:
                    if timerw1[1] > 3:
                        move(i,dif,1.5*vel)

    elif horda == 2:
        for inim in range(len(inimigos)):
            for i in inimigos[inim]:
                i.draw()
                if inim == 0 :
                    if timerw2[0] > 0:
                        move(i,dif,1*vel)
                elif inim == 1:
                    if timerw2[1] > 0:
                        move(i,dif,1.5*vel)
                elif inim == 2:
                    if timerw2[2] > 0:
                        move(i,dif,2*vel)

    elif horda == 3:
        for inim in range(len(inimigos)):
            for i in inimigos[inim]:
                i.draw()
                if inim == 0 :
                    if timerw3[0] > 0:
                        move(i,dif,1*vel)
                elif inim == 1:
                    if timerw3[1] > 0:
                        move(i,dif,1.5*vel)
                elif inim == 2:
                    if timerw3[2] > 0:
                        move(i,dif,2*vel)
                elif inim == 3:
                    if timerw3[3] > 0:
                        move(i,dif,2.5*vel)

    elif horda == 4:
        for inim in range(len(inimigos)):
            for i in inimigos[inim]:
                i.draw()
                if inim == 0:
                    if timerw4[0] > 0:
                        move(i, dif, 1 * vel)
                elif inim == 1:
                    if timerw4[1] > 0:
                        move(i, dif, 1.5 * vel)
                elif inim == 2:
                    if timerw4[2] > 0:
                        move(i, dif, 2 * vel)
                elif inim == 3:
                    if timerw4[3] > 0:
                        move(i, dif, 2.5 * vel)
                elif inim == 4:
                    if timerw4[4] > 0:
                        move(i, dif, 3 * vel)

    elif horda == 5:
        for inim in range(len(inimigos)):
            for i in inimigos[inim]:
                i.draw()
                if inim == 0:
                    if timerw5[0] > 0:
                        move(i, dif, 1 * vel)
                elif inim == 1:
                    if timerw5[1] > 0:
                        move(i, dif, 1.5 * vel)
                elif inim == 2:
                    if timerw5[2] > 0:
                        move(i, dif, 2 * vel)
                elif inim == 3:
                    if timerw5[3] > 0:
                        move(i, dif, 2.5 * vel)
                elif inim == 4:
                    if timerw5[4] > 0:
                        move(i, dif, 3 * vel)
                elif inim == 5:
                    if timerw5[5] > 0:
                        move(i, dif, 1 * vel)


    return None

def dist(a,b):

    x = abs(a.x - (b.x + b.width/2))
    y = abs(a.y - (b.y + b.height/2))
    dis = (x**2 + y**2)**0.5

    return dis

def comprar(ally,allys,gd):
    global gold
    global timercomp
    global selectedlan
    global selectedarq
    global selectedcat
    global selectedesp
    global selectedpal
    nm = ""
    slc = 6
    if ally == paladino:
        nm = "paladinoCima.png"
        slc = 0
    elif ally == catapulta:
        nm = "catapulta.png"
        slc = 1
    elif ally == espadachim:
        nm = "espadachinCima.png"
        slc = 2
    elif ally == lanceiro:
        nm = "lanceiroCima.png"
        slc = 3
    elif ally == arqueiro:
        nm = "arqueiroCima.png"
        slc = 4
    if Mouse().is_over_area((ally.x, ally.y), (ally.x + ally.width, ally.y + ally.height)):
        if Mouse().is_button_pressed(1) and timercomp > 1 and gold >= gd and not True in [selectedpal,selectedesp,
                                                                                          selectedcat,selectedarq,selectedarq]:
            allys.append(Sprite(str(nm)))
            if slc == 0:
                selectedpal = True
            elif slc == 1:
                selectedcat = True
            elif slc == 2:
                selectedesp = True
            elif slc == 3:
                selectedlan = True
            elif slc == 4:
                selectedarq = True
            gold -= gd
            timercomp = 0
    return None

def posicionar(pos):
    global selectedarq
    global selectedesp
    global selectedcat
    global selectedlan
    global selectedpal
    global timebuy
    timebuy = 0
    timebuy += janela.delta_time()
    if selectedarq == True and timebuy < 2:
        arqueiros[len(arqueiros) - 1].x = pos[0]
        arqueiros[len(arqueiros) - 1].y = pos[1]
    elif selectedesp == True:
        espadachins[len(espadachins) - 1].x = pos[0]
        espadachins[len(espadachins) - 1].y = pos[1]
    elif selectedpal == True:
        paladinos[len(paladinos) - 1].x = pos[0]
        paladinos[len(paladinos) - 1].y = pos[1]
    elif selectedlan == True:
        lanceiros[len(lanceiros) - 1].x = pos[0]
        lanceiros[len(lanceiros) - 1].y = pos[1]
    elif selectedcat == True:
        catapultas[len(catapultas) - 1].x = pos[0]
        catapultas[len(catapultas) - 1].y = pos[1]
    return None

score = 0

raio = 75
global gold
global vel
global dif
global timerw1
global timerw2
global timerw3
global timerw4
global timerw5
global paladinos
global arqueiros
global espadachins
global lanceiros
global catapultas
global timebuy

pygame.display.set_icon(pygame.image.load('icon.png'))

w = 800
h = 600

gold = 600

white = (255, 255, 255)
grey = (200, 200, 200)

janela = Window(w, h)

background = GameImage('fundo.jpg')

bgmenu = GameImage("bgmenutd.png")

timebuy = 0

musicbt = Sprite("musicon.png")
musicbt.set_position(765,5)

enemy = criawave()

teste = [0,1,4,6,7]

select = 1
mus = 1
dif = 1

vel = 1

timerw1 = [0,-7]
timerw2 = [0,0,0]
timerw3 = [0,0,0,0]
timerw4 = [0,0,0,0,0]
timerw5 = [0,0,0,0,0,0]

w1ok = False
w2ok = False
w3ok = False
w4ok = False
w5ok = False

timer1 = 0

tickpress = 2
tickmus = 2

tick = 10

cad = 1

wave = 1

timercomp = 0

paladino = Sprite("paladino.png")
paladino.set_position(670,130)
timerpal = 0
paladinos = []
cadpal = 2
espadachim = Sprite("espadachin.png")
espadachim.set_position(670,180)
timeresp = 0
espadachins = []
cadesp = 2
arqueiro = Sprite("arqueiro.png")
arqueiro.set_position(740,180)
timerarq = 0
arqueiros = []
cadarq = 1
lanceiro = Sprite("lanceiro.png")
lanceiro.set_position(740,130)
timerlan = 0
lanceiros = []
cadlan = 2
catapulta = Sprite("catapulta.png")
catapulta.set_position(705,230)
timercat = 0
catapultas = []
cadcat = 3

selected = False
selectedlan = False
selectedarq = False
selectedesp = False
selectedpal = False
selectedcat = False

bgmusic = Sound("bgmusic.ogg")
bgmusic.set_volume(40)
bgmusic.play()

font = "Candara"

vida = 100

running = False
menu = True
resume = False
config = False

caminho = Sprite("caminho.png")

statemouse = False

# --------------------------------------MENU-------------------------------------- #

while menu:
    bgmenu.draw()
    janela.set_title("MENU")

    if Mouse().is_over_area((40,400),(120,430)):
        select = 1

    elif Mouse().is_over_area((40,440),(235,470)):
        select = 2

    elif Mouse().is_over_area((40,480),(95,510)):
        select = 3


    if select == 1:
        janela.draw_text(">Iniciar", 40, 400, 30, white, font)
        janela.draw_text("Configurações", 40, 440, 30, grey, font)
        janela.draw_text("Sair", 40, 480, 30, grey, font)
        if Mouse().is_button_pressed(1) and Mouse().is_over_area((40,400),(120,430)):
            resume = True
            running = True

    elif select == 2:
        janela.draw_text("Iniciar", 40, 400, 30, grey, font)
        janela.draw_text(">Configurações", 40, 440, 30, white, font)
        janela.draw_text("Sair", 40, 480, 30, grey, font)
        if Mouse().is_button_pressed(1) and Mouse().is_over_area((40,440),(235,470)):
            config = True

    elif select == 3:
        janela.draw_text("Iniciar", 40, 400, 30, grey, font)
        janela.draw_text("Configurações", 40, 440, 30, grey, font)
        janela.draw_text(">Sair", 40, 480, 30, white, font)
        if Mouse().is_button_pressed(1) and Mouse().is_over_area((40,480),(95,510)):
            menu = False

    janela.update()

    while config:
        janela.set_title("Configurações")
        bgmenu.draw()
        janela.draw_text("Música:", 40, 400, 30, grey, font)

        if mus == 1:
            janela.draw_text("On", 150, 400, 30, white, font)
            janela.draw_text("Off", 200, 400, 30, grey, font)
            bgmusic.unpause()

        elif mus == 2:
            janela.draw_text("On", 150, 400, 30, grey, font)
            janela.draw_text("Off", 200, 400, 30, white, font)
            bgmusic.pause()

        if Mouse().is_over_area((150,400),(190,430)) and Mouse().is_button_pressed(1):
            mus = 1

        elif Mouse().is_over_area((200,400),(250,430)) and Mouse().is_button_pressed(1):
            mus = 2

        if Mouse().is_over_area((205,440),(275,470)) and Mouse().is_button_pressed(1):
            dif = 1

        elif Mouse().is_over_area((276,440),(395,470)) and Mouse().is_button_pressed(1):
            dif = 2

        elif Mouse().is_over_area((400,440),(470,470)) and Mouse().is_button_pressed(1):
            dif = 3


        janela.draw_text("Dificuldade:", 40, 440, 30, grey, font)

        if dif == 1:
            janela.draw_text("Easy", 205, 440, 30, white, font)
            janela.draw_text("Medium", 276, 440, 30, grey, font)
            janela.draw_text("Hard", 400, 440, 30, grey, font)

        if dif == 2:
            janela.draw_text("Easy", 205, 440, 30, grey, font)
            janela.draw_text("Medium", 276, 440, 30, white, font)
            janela.draw_text("Hard", 400, 440, 30, grey, font)

        if dif == 3:
            janela.draw_text("Easy", 205, 440, 30, grey, font)
            janela.draw_text("Medium", 276, 440, 30, grey, font)
            janela.draw_text("Hard", 400, 440, 30, white, font)


        janela.draw_text("Aperte ESC para voltar", 40, 480, 30, grey, font)
        if Keyboard().key_pressed("esc"):
            config = False

        janela.update()


# ------------------------------------PAUSE------------------------------------ #

    while resume:
        janela.set_title("PAUSED")
        janela.draw_text("PAUSED: Enter to resume!", w / 2 - 300, 270, size=50, color=(255, 0, 0), font_name="Candara")
        if Keyboard().key_pressed("enter"):
            running = True

        janela.update()

# -----------------------------------JOGO-------------------------------------- #

        while running:
            janela.set_title("LEVEL 1")
            background.draw()
            caminho.draw()
            musicbt.draw()

            paladino.draw()
            lanceiro.draw()
            arqueiro.draw()
            catapulta.draw()
            espadachim.draw()

            posicionar(Mouse().get_position())

            for i in arqueiros:
                i.draw()

            for i in paladinos:
                i.draw()

            for i in lanceiros:
                i.draw()

            for i in catapultas:
                i.draw()

            for i in espadachins:
                i.draw()


            if selectedarq:
                if Mouse().is_button_pressed(3):
                    selectedarq = False
            elif selectedpal:
                if Mouse().is_button_pressed(3):
                    selectedpal = False
            elif selectedlan:
                if Mouse().is_button_pressed(3):
                    selectedlan = False
            elif selectedesp:
                if Mouse().is_button_pressed(3):
                    selectedesp = False
            elif  selectedcat:
                if Mouse().is_button_pressed(3):
                    selectedcat = False

            timerpal += janela.delta_time()
            timercat += janela.delta_time()
            timerlan += janela.delta_time()
            timeresp += janela.delta_time()
            timerarq += janela.delta_time()
            timercomp += janela.delta_time()

            timebuy += janela.delta_time()

            timer1 += janela.delta_time()

            timerw1[0] += janela.delta_time()
            timerw1[1] += janela.delta_time()
            timerw2[0] += janela.delta_time()
            timerw2[1] += janela.delta_time()
            timerw2[2] += janela.delta_time()
            timerw3[0] += janela.delta_time()
            timerw3[1] += janela.delta_time()
            timerw3[2] += janela.delta_time()
            timerw3[3] += janela.delta_time()
            timerw4[0] += janela.delta_time()
            timerw4[1] += janela.delta_time()
            timerw4[2] += janela.delta_time()
            timerw4[3] += janela.delta_time()
            timerw4[4] += janela.delta_time()
            timerw5[0] += janela.delta_time()
            timerw5[1] += janela.delta_time()
            timerw5[2] += janela.delta_time()
            timerw5[3] += janela.delta_time()
            timerw5[4] += janela.delta_time()
            timerw5[5] += janela.delta_time()

            tickpress += janela.delta_time()
            tickmus += janela.delta_time()

            movehorda(1,enemy[0])
            if wave == 2:
                movehorda(2,enemy[1])

            if wave == 3:
                movehorda(3,enemy[2])

            if wave == 4:
                movehorda(4,enemy[3])

            if wave == 5:
                movehorda(5,enemy[4])

            #print(Mouse().get_position())

            for i in paladinos:
                for j in enemy:
                    for k in j:
                        for t in k:
                            if dist(t,i) <= 75 and timerpal > (1/vel)*cadpal:
                                k.remove(t)
                                timerpal = 0
                                gold += 5
            for i in arqueiros:
                for j in enemy:
                    for k in j:
                        for t in k:
                            if dist(t,i) <= 150 and timerarq > (1/vel)*cadarq:
                                k.remove(t)
                                timerarq = 0
                                gold += 5

            for i in lanceiros:
                for j in enemy:
                    for k in j:
                        for t in k:
                            if dist(t,i) <= 60 and timerlan > (1/vel)*cadlan:
                                k.remove(t)
                                timerlan = 0
                                gold += 5

            for i in espadachins:
                for j in enemy:
                    for k in j:
                        for t in k:
                            if dist(t,i) <= 60 and timeresp > (1/vel)*cadesp:
                                k.remove(t)
                                timeresp = 0
                                gold += 5

            for i in catapultas:
                for j in enemy:
                    for k in j:
                        for t in k:
                            if dist(t,i) <= 150 and timercat > (1/vel)*cadcat:
                                k.remove(t)
                                timercat = 0
                                gold += 5


            janela.draw_text("Ouro:" + str(gold), 658, 10, 26, white, "Candara")
            janela.draw_text("Onda:" + str(wave), 658, 38, 26, white, "Candara")
            janela.draw_text("Vidas:" + str(vida), 658, 66, 26, white, "Candara")

            if Mouse().is_over_area((musicbt.x,musicbt.y),(musicbt.x + musicbt.width,musicbt.y + musicbt.height)):
                if Mouse().is_button_pressed(1) and tickmus > 1:
                    if bgmusic.is_playing():
                        musicbt = Sprite("musicoff.png")
                        musicbt.set_position(765,5)
                        bgmusic.pause()
                        tickmus = 0
                    else:
                        musicbt = Sprite("musicon.png")
                        musicbt.set_position(765,5)
                        bgmusic.unpause()
                        tickmus = 0

            if vida <= 0:
                running = False
                resume = False

            if Keyboard().key_pressed("w") and vel <= 4 and tickpress > 1:
                vel *= 2
                tickpress = 0

            if Keyboard().key_pressed("s") and vel >= 1 and tickpress > 1:
                vel /= 2
                tickpress = 0

            if timer1 <= 3:
                janela.draw_text(str(int(abs(4-timer1))),360,260,50,(100,200,50))

            if Keyboard().key_pressed("esc"):
                running = False

            comprar(paladino,paladinos,200)
            comprar(lanceiro,lanceiros,100)
            comprar(arqueiro,arqueiros,150)
            comprar(catapulta,catapultas,300)
            comprar(espadachim,espadachins,150)


            tick += janela.delta_time()

            for i in enemy[0]:
                for j in i:
                    if j.x <= 0 and 400 < j.y < 800 :
                        vida -= 1
                        i.remove(j)

            for i in enemy[1]:
                for j in i:
                    if j.x <= 0 and 400 < j.y < 800 :
                        vida -= 1
                        i.remove(j)

            for i in enemy[2]:
                for j in i:
                    if j.x <= 0 and 400 < j.y < 800 :
                        vida -= 1
                        i.remove(j)

            for i in enemy[3]:
                for j in i:
                    if j.x <= 0 and 400 < j.y < 800 :
                        vida -= 1
                        i.remove(j)

            for i in enemy[4]:
                for j in i:
                    if j.x <= 0 and 400 < j.y < 800 :
                        vida -= 1
                        i.remove(j)

            if enemy[0] == [[],[]] and not w1ok:
                wave += 1
                timerw2 = [0, -5, -7]
                w1ok = True

            if enemy[1] == [[],[],[]] and not w2ok:
                wave += 1
                timerw3 = [0, -5, -7, -10]
                w2ok = True

            if enemy[2] == [[],[],[],[]] and not w3ok:
                wave += 1
                timerw4 = [0, -5, -7, -10, -12]
                w3ok = True

            if enemy[3] == [[],[],[],[],[]] and not w4ok:
                wave += 1
                timerw5 = [0, -5, -7, -10, -12, -15]
                w4ok = True

            if enemy[4] == [[],[],[],[],[],[]]:
                if vida == 100:
                    score *= 2
                running = False
                resume = False

            janela.update()