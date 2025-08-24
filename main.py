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



pgzrun.go()