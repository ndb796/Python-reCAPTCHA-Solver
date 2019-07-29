#-*- coding:utf-8 -*-

import time
import pyautogui
import random

print(pyautogui.position().x)
SEARCH_COORDS = (320, 55) # 검색 창 위치
PREVIOUS_COORDS = (90, 600) # 버튼 전에 도달해야 하는 위치가 있다고 가정
BUTTON_COORDS = (200, 880) # 어떤 버튼이 존재하는 위치


def get_position():
    return pyautogui.position().x, pyautogui.position().y


# 특정한 위치로 지그재그로 마우스를 흔들면서 이동하는 함수
def go(target_x, target_y):
    while True:
        x, y = get_position()
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


while True:
    pyautogui.moveTo(SEARCH_COORDS)
    time.sleep(1.0)
    pyautogui.click()
    pyautogui.typewrite('http://dongbin.tk/v3')
    pyautogui.press('enter')

    time.sleep(1.0)
    go(PREVIOUS_COORDS[0], PREVIOUS_COORDS[1])
    pyautogui.click()

    time.sleep(1.0)
    go(BUTTON_COORDS[0], BUTTON_COORDS[1])
    pyautogui.click()