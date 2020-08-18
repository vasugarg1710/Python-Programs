from pygame import mixer
from time import time
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


watersecs = 30*60
eyesecs = 40*60
physical = 50*60

while True:
    if time()-initwater > watersecs:
        loop_music("water.mp3")
        stopper("water")
        initwater = time()

    if time()-initeyes > eyesecs:
        loop_music("eyes.mp3")
        stopper("eyes")
        initeyes = time()

    if time()-initphysical > physical:
        loop_music("physical.mp3")
        stopper("physical")
        initphysical = time()


