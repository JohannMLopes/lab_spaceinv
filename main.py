from PPlay.window import *
from PPlay.sprite import *

def dificult(diff):

    janela = Window(800, 600)
    mouse = janela.get_mouse()

    facil = Sprite("menu/facil.png")
    medio = Sprite("menu/medio.png")
    dificil = Sprite("menu/dificil.png")

    facil.x = janela.width/2 - facil.width/2
    facil.y = 50

    medio.x = janela.width/2 - medio.width/2
    medio.y = facil.y + medio.height + 50

    dificil.x = janela.width/2 - dificil.width/2
    dificil.y = medio.y + dificil.height + 50

    while True:
        if mouse.is_over_area([facil.x,facil.y],[facil.x + facil.width, facil.y + facil.height]) and mouse.is_button_pressed(1):
            diff = 1
            return diff
        if mouse.is_over_area([medio.x, medio.y],[medio.x + medio.width, medio.y + medio.height]) and mouse.is_button_pressed(1):
            diff = 2
            return diff
        if mouse.is_over_area([dificil.x, dificil.y],[dificil.x + dificil.width, dificil.y + dificil.height]) and mouse.is_button_pressed(1):
            diff = 3
            return diff
        janela.set_background_color([255, 255, 255])
        facil.draw()
        medio.draw()
        dificil.draw()
        janela.update()

def spaceinv():

    janela = Window(800, 600)
    teclado = janela.get_keyboard()
    nave = Sprite("game/spc_ship.png")
    tiro = False

    # Inicia objetos

    nave.x = janela.width/2 - nave.width/2
    nave.y = janela.height - nave.height - 10

    while True:

        if teclado.key_pressed("esc"):
            break

        # Colisão
        if nave.x <= 0:
            nave.x = 0
        if nave.x >= janela.width - nave.width:
            nave.x = janela.width - nave.width

        # Tiro
        if teclado.key_pressed("space"):
            tiro = Sprite("game/laser.png")
            tiro.y = nave.y - tiro.height
            tiro.x = nave.x + nave.width/2 - tiro.width/2

        if tiro == True:
            if tiro.y < 0-tiro.height:
                tiro = False
            tiro.x += 200 * janela.delta_time()

        # Movimento da nave
        if teclado.key_pressed("left"):
            nave.x -= 100 * janela.delta_time()
        if teclado.key_pressed("right"):
            nave.x += 100 * janela.delta_time()

        if tiro == True:
            tiro.draw()
        janela.set_background_color([0, 0, 0])
        nave.draw()
        janela.update()

#MAIN

janela = Window(800, 600)
janela.set_title("Game")
teclado = janela.get_keyboard()

# INICIA RECURSOS
janela = Window(800, 600)
janela.set_title("SpaceInv")

mouse = janela.get_mouse()

# INICIA OPÇOES MENU
play = Sprite("menu/play.png")
diff = Sprite("menu/diff.png")
ranking = Sprite("menu/rank.png")
sair = Sprite("menu/exit.png")

play.x = 50
play.y = 20

diff.x = 50
diff.y = play.y + diff.height + 20

ranking.x = 50
ranking.y = diff.y + ranking.height + 20

sair.x = 50
sair.y = ranking.y + sair.height + 20

dificuldade = 1

# GAMELOOP
while True:

    if mouse.is_over_area([diff.x, diff.y], [diff.x + diff.width, diff.y + diff.height]) and mouse.is_button_pressed(1):
        dificuldade = dificult(dificuldade)

    if mouse.is_over_area([play.x, play.y], [play.x + play.width, play.y + play.height]) and mouse.is_button_pressed(1):
        spaceinv()

    if mouse.is_over_area([sair.x, sair.y], [sair.x + sair.width, sair.y + sair.height]) and mouse.is_button_pressed(1):
        break

    janela.set_background_color([255, 255, 255])
    play.draw()
    diff.draw()
    ranking.draw()
    sair.draw()
    janela.draw_text("%d" % dificuldade,400, 50, 24, [0, 0, 0], "Arial", False, False)
    janela.update()
