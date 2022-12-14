from PPlay.window import *
from PPlay.sprite import *
import random

def dificult():

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
            diff = 1.5
            return diff
        if mouse.is_over_area([dificil.x, dificil.y],[dificil.x + dificil.width, dificil.y + dificil.height]) and mouse.is_button_pressed(1):
            diff = 2
            return diff
        janela.set_background_color([255, 255, 255])
        facil.draw()
        medio.draw()
        dificil.draw()
        janela.update()

def spaceinv(dificuldade):

    janela = Window(800, 600)
    teclado = janela.get_keyboard()
    nave = Sprite("game/spc_ship.png")
    vtiro = []
    venemy = []
    menemy = []
    velenemy = 50
    tcont = 1.0
    ct = 0.0
    fps = 0
    cfps = 0
    points = 0
    boss_set = False
    boss_life = 3
    random.seed(5)

    # Inicia objetos

    nave.x = janela.width/2 - nave.width/2
    nave.y = janela.height - nave.height - 10

    for i in range(0, 3):
        for j in range(0,4):
            if random.randint(0, 1) == 1 and boss_set == False:
                boss = Sprite("game/boss.png")
                boss.x = 10 + (boss.width * j)
                boss.y = 10 + (boss.height * i)
                venemy.append(boss)
                boss_set = True
            elif i == 2 and j == 3 and boss_set == False:
                boss = Sprite("game/boss.png")
                boss.x = 10 + (boss.width * j)
                boss.y = 10 + (boss.height * i)
                venemy.append(boss)
                boss_set = True
            else:
                enemy = Sprite("game/enemy.png")
                enemy.x = 10 + (enemy.width * j)
                enemy.y = 10 + (enemy.height * i)
                venemy.append(enemy)
        menemy.append(venemy)

    # GameLoop

    while True:

        hit = False
        tcont += janela.delta_time()
        ct += janela.delta_time()
        fps += 1
        if ct > 1.0:
            cfps = fps
            fps = 0
            ct = 0.0

        if teclado.key_pressed("esc"):
            break

        # Colis??o
        if nave.x <= 0:
            nave.x = 0
        if nave.x >= janela.width - nave.width:
            nave.x = janela.width - nave.width

        # Tiro
        if teclado.key_pressed("space") and tcont > 1.0 * dificuldade:
            tiro = Sprite("game/laser.png")
            tiro.y = nave.y - tiro.height
            tiro.x = nave.x + nave.width/2 - tiro.width/2
            vtiro.append(tiro)
            tcont = 0.0

        for i in range(len(vtiro)):
            if vtiro[i].y < 0 - tiro.height:
                vtiro.pop(i)
                break

        for i in range(len(vtiro)):
            vtiro[i].y -= 500 * janela.delta_time()

        # Hit

        for i in range(len(vtiro)):
            if vtiro[i].y <= venemy[-1].y + enemy.height:
                for j in range(len(menemy)):
                    for k in range(len(venemy)):
                        if vtiro[i].collided(venemy[k]):
                            if venemy[k] == boss:
                                if boss_life == 2:
                                    hit = True
                                    boss = enemy
                                    boss_life -= 1
                                    vtiro.pop(i)
                                    break
                                else:
                                    hit = True                                    
                                    boss_life -= 1
                                    vtiro.pop(i)
                                    break
                            else:
                                hit = True
                                points += 10 * dificuldade
                                venemy.pop(k)
                                vtiro.pop(i)
                                break
                    if hit:
                        break
            if hit:
                break

        # Reset/New phase

        if menemy == [[], [], []]:
            boss_set = False
            boss_life = 3
            for i in range(len(vtiro)):
                vtiro.pop(0)         
            for i in range(0, 3):
                for j in range(0,4):
                    if random.randint(0, 1) == 1 and boss_set == False:
                        enemy = Sprite("game/boss.png")
                        enemy.x = 10 + (enemy.width * j)
                        enemy.y = 10 + (enemy.height * i)
                        venemy.append(enemy)
                        boss_set = True
                    elif i == 2 and j == 3 and boss_set == False:
                        enemy = Sprite("game/boss.png")
                        enemy.x = 10 + (enemy.width * j)
                        enemy.y = 10 + (enemy.height * i)
                        venemy.append(enemy)
                        boss_set = True
                    else:
                        enemy = Sprite("game/enemy.png")
                        enemy.x = 10 + (enemy.width * j)
                        enemy.y = 10 + (enemy.height * i)
                        venemy.append(enemy)
                menemy[i] = venemy
            dificuldade = dificuldade + 0.5



        # Movimento da nave

        if teclado.key_pressed("left"):
            nave.x -= 100 * janela.delta_time()
        if teclado.key_pressed("right"):
            nave.x += 100 * janela.delta_time()

        # Inimigos

        if menemy != [[], [], []]:
            for i in range(len(menemy)):
                for j in range(len(venemy)):
                    if venemy[j].x > janela.width - enemy.width:
                        for k in range(len(venemy)):
                            venemy[k].y += 5000 * janela.delta_time()
                        velenemy = -50
                        venemy[j].x = janela.width - enemy.width
                    if venemy[j].x < 0:
                        for k in range(len(venemy)):
                            venemy[k].y += 5000 * janela.delta_time()
                        velenemy = 50
                        venemy[j].x = 0
                    if venemy[j].y >= nave.y - enemy.height:
                        janela.draw_text("YOU LOST", 400, 50, 72, [255, 255, 255], "Arial", True, False)
                        name = input("Write your name: ")
                        points = str(points)
                        rank.write(name + " " + points + "\n")
                        return
                    venemy[j].x += velenemy * janela.delta_time()
            
        
        janela.set_background_color([0, 0, 0])
        nave.draw()
        for i in range(len(vtiro)):
            vtiro[i].draw()
        for i in range(len(menemy)):
            for j in range(len(venemy)):
                venemy[j].draw()
        janela.draw_text("Pontos: %d" % points,             30, 10, 12, [255, 255, 255], "Arial", False, False)
        janela.draw_text("%d" % cfps, janela.width - 30, 10, 12, [255, 255, 255], "Arial", False, False)
        janela.update()

#MAIN

janela = Window(800, 600)
janela.set_title("Game")
teclado = janela.get_keyboard()

# INICIA RECURSOS
janela = Window(800, 600)
janela.set_title("SpaceInv")

mouse = janela.get_mouse()

rank = open("rank.txt", "a")

# INICIA OP??OES MENU
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
        dificuldade = dificult()

    if mouse.is_over_area([play.x, play.y], [play.x + play.width, play.y + play.height]) and mouse.is_button_pressed(1):
        spaceinv(dificuldade)

    if mouse.is_over_area([sair.x, sair.y], [sair.x + sair.width, sair.y + sair.height]) and mouse.is_button_pressed(1):
        break

    janela.set_background_color([255, 255, 255])
    play.draw()
    diff.draw()
    ranking.draw()
    sair.draw()
    janela.draw_text("%.1f" % dificuldade, 400, 50, 24, [0, 0, 0], "Arial", False, False)
    janela.update()
