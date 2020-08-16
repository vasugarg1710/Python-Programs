from time import time

initial_eyes = time()
eyes_sec = 30 * 60
while True:
    if time() - initial_eyes > eyes_sec:
        print("Do eye exercise")
        initial_eyes = time()
