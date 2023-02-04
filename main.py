# https://fivesjs.skipser.com/trex-game/

import pyautogui
from PIL import ImageGrab, ImageOps
from time import sleep

pyautogui.hotkey("alt", "tab")
pyautogui.hotkey("ctrl", "1")
pyautogui.keyDown('up')
sleep(0.001)
pyautogui.keyUp('up')
sleep(0.001)

target = (1070, 447, 1120, 473)


def image_grab():
    image = ImageGrab.grab(target)
    gray_image = ImageOps.grayscale(image)
    # gray.save("dino.jpg")
    colors = sum(map(sum, gray_image.getcolors()))
    return colors


def jump():
    pyautogui.keyDown('up')
    sleep(0.001)
    pyautogui.keyUp('up')


on = True
while on:
    if image_grab() != 1547:
        jump()
