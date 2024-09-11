import time
import random
import pyautogui as pg

animals = ("dog", "cat", "mouse", "rabbit")

time.sleep(10)

for i in range(50):
    anml = random.choice(animals)
    pg.write("You are a " + anml)
    pg.press("enter")
