import pgzrun
from time import time
from random import randint

WIDTH = 800
HEIGHT = 600
TITLE = "Connecting Sheep"

sheep_number = randint(5,21)
start_time = 0
total_time = 0
current_sheep = 0

sheep = []
lines = []

def making_sheep():
    global start_time, sheep_number
    for i in range(sheep_number):
        she = Actor("sheep")
        she.pos = randint(40,640),randint(40,540)
        sheep.append(she)
    start_time = time()

def draw():
    global total_time
    screen.blit("meadow.jpg",(0,0))
    num=1
    for she in sheep:
        she.draw()
        screen.draw.text(str(num),(she.pos[0],she.pos[1]+20))
        num= num+1
    
    for line in lines:
        screen.draw.line(line[0],line[1],"white")
    
    if current_sheep<sheep_number:
        total_time = time()-start_time
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)
    else:
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)

        



def update():
    pass

def on_mouse_down(pos):
    global lines,current_sheep
    if current_sheep<sheep_number:
        if sheep[current_sheep].collidepoint(pos):
            if current_sheep>0:
                lines.append((sheep[current_sheep-1].pos,sheep[current_sheep].pos))
            current_sheep = current_sheep+1
        else:
            current_sheep = 0
            lines = []


making_sheep()
pgzrun.go()
