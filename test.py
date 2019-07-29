#-*- coding:utf-8 -*-

import time
import pyautogui
import random

print(pyautogui.position().x)
SEARCH_COORDS = (320, 70)
CAPTCHA_COORDS = (90, 600)
AUDIO_COORDS = (200, 880)


def get_position():
    return pyautogui.position().x, pyautogui.position().y


def go(target_x, target_y):
    while True:
        x, y = get_position()
        # time.sleep(0.001)
        sign_x = target_x - x
        sign_y = target_y - y
        if sign_x <= 15 and sign_y <= 15:
            break
        if sign_x >= 0:
            x += 14 + random.randrange(-3, 4)
        elif sign_x < 0:
            x -= 14 + random.randrange(-3, 4)
        if sign_y >= 0:
            y += 14 + random.randrange(-3, 4)
        elif sign_y < 0:
            y -= 14 + random.randrange(-3, 4)
        pyautogui.moveTo(x, y)


pyautogui.moveTo(SEARCH_COORDS)
pyautogui.click()
pyautogui.typewrite('https://www.google.com/recaptcha/api2/demo')
pyautogui.press('enter')

go(CAPTCHA_COORDS[0], CAPTCHA_COORDS[1])
pyautogui.click()

# 이 지점에서 캡차 끝날 수도 있음.
# 사이트에 연속적으로 들어가는 것 아니라면, 성공 가능성 높음

time.sleep(1.0)
go(AUDIO_COORDS[0], AUDIO_COORDS[1])
pyautogui.click()

'''
SEARCH_COORDS = (320, 70)
CAPTCHA_COORDS = (90, 600)
CAPTCHA_COORDS = (90, 600)

print("Visiting Demo Site")
pyautogui.moveTo(SEARCH_COORDS)
pyautogui.click()
pyautogui.typewrite('https://www.google.com/recaptcha/api2/demo')
pyautogui.press('enter')

print(pyautogui.position())

time.sleep(3)
pyautogui.moveTo(CAPTCHA_COORDS)
pyautogui.click()

'''