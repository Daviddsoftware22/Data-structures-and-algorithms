import time
import random
import math
import os


def turn_off(y):
    print(f"From now {time.ctime()}")
    if y > 60 :
        print(f"Your computer will shut down in {math.trunc(y / 60)} minutes")
    else:
        print("Your computer will shut down in less than 0 minutes")
    while y > 0 :
        y -= 1
        time.sleep(1)
        if y < 30:
            print(f"Your computer will shut down in : {y} seconds")
    os.system("shutdown /s /t 1")
