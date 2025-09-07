import pgzrun
from time import time
from random import randint

WIDTH = 800
HEIGHT = 600
TITLE = "Connecting Satellites"

satellites_count = 10
start_time = 0
total_time = 0
current_sat = 0

satellites = []
lines = []

def create_sats():
    global start_time, satellites_count
    for i in range(satellites_count):
        sat = Actor("satellite")
        sat.pos = randint(40,640),randint(40,540)
        satellites.append(sat)
    start_time = time()

def draw():
    global total_time
    screen.blit("bg.png",(0,0))
    num=1
    for sat in satellites:
        sat.draw()
        screen.draw.text(str(num),(sat.pos[0],sat.pos[1]+20))
        num= num+1
    
    for line in lines:
        screen.draw.line(line[0],line[1],"white")
    
    if current_sat<satellites_count:
        total_time = time()-start_time
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)
    else:
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)

        



def update():
    pass

def on_mouse_down(pos):
    global lines,current_sat
    if current_sat<satellites_count:
        if satellites[current_sat].collidepoint(pos):
            if current_sat>0:
                lines.append((satellites[current_sat-1].pos,satellites[current_sat].pos))
            current_sat = current_sat+1
        else:
            current_sat = 0
            lines = []


create_sats()
pgzrun.go()