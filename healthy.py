from pygame import mixer
from time import time
from datetime import datetime
initwater = time()
initeyes = time()
initphysical = time()
def loop_music(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(loops=1000)

def stopper(stop):
    stops = input(f"Enter {stop} to stop the music")
    if stops == stop:
        mixer.music.stop()

def log_now(file,msg):
    with open(file,"a") as f:
        f.write(f"\n{msg} {datetime.now()}")


watersecs = 30*60
eyesecs = 40*60
physical = 50*60

print("Started program")

while True:
    if time()-initwater > watersecs:
        loop_music(r"C:\Users\vasug\PycharmProjects\Python\water.mp3")
        stopper("water")
        log_now("water.txt", "Drank water at")
        initwater = time()


    if time()-initeyes > eyesecs:
        loop_music(r"C:\Users\vasug\PycharmProjects\Python\eyes.mp3")
        stopper("eyes")
        log_now("eyes.txt", "Eyes relaxed at")
        initeyes = time()

    if time()-initphysical > physical:
        loop_music(r"C:\Users\vasug\PycharmProjects\Python\physical.mp3")
        stopper("physical")
        log_now("eyes.txt", "Done physical exercise at")
        initphysical = time()


