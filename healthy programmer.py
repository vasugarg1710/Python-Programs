import time
def reminder(partofbody,timeinsec):
    import datetime
    from pygame import mixer
    mixer.init()
    mixer.music.load(f"{partofbody}.mp3")
    mixer.music.play(loops=1000)
    while True:
        print(f"Enter {partofbody} to stop the sound.")
        query = input()
        if query == partofbody:
            mixer.music.stop()
            f = open(f"{partofbody}.txt","a")
            f.write(f"Taken care of {partofbody} on {datetime.datetime.now()}")
            f.write("\n")
            f.close()
            time.sleep(timeinsec)
            break


while True:
    reminder("eyes", 30*60) # after 30 min running
    reminder("water", 20 * 60) # 18 water glasses in 6 hours, i want every 20 min
    reminder("phsical",45 * 60)




