import time
import pyautogui as auto
import random


TIMES = 0
ROOMSTART = 0
ROOMACCEPT = 0
STAGE1_1 = 0
STAGE2_4 = 0
INGAME = 0

def clear_par():
    global TIMES
    TIMES += 1
    print("已完成 " + str(TIMES) + ' 局')


def on_click(x, y, button):
    auto.mouseDown(x=x, y=y, button=button)
    auto.mouseUp(x=x, y=y, button=button, duration=1)
    auto.mouseDown(x=x, y=y, button=button)
    auto.mouseUp(x=x, y=y, button=button, duration=1)


def room_start():
    global INGAME
    picture = auto.locateOnScreen('assert/roomStart.png')
    if picture is not None:
        INGAME = 0
        print("点击寻找对局")
        auto.moveTo(picture)
        auto.click(clicks=2, interval=1)


def room_accept():
    on_click(952, 715, 'left')


def draft_stage(stage):
    global INGAME
    picture = auto.locateOnScreen(stage)
    if picture is not None:
        INGAME = 1
        x = random.randint(800, 1300)
        y = random.randint(200, 700)
        on_click(x, y, 'right')
        print("走走 " + str(x) + " " + str(y))


def room_end():
    picture = auto.locateOnScreen('assert/roomEnd.png')
    if picture is not None:
        print("点击再来一盘")
        auto.moveTo(picture)
        auto.click(clicks=2, interval=1)
        clear_par()


def ff_stage(stage):
    global INGAME
    picture = auto.locateOnScreen(stage)
    if picture is not None:
        print("准备认输")
        on_click(1902, 851, 'left')
        on_click(759, 856, 'left')
        on_click(856, 476, 'left')
        INGAME = 0


def in_game_stage(i):
    global INGAME

    picture = auto.locateOnScreen('assert/inGameTag.bmp')
    if picture is not None:
        INGAME = 1
        if i % 20 == 3:
            print("升级")
            on_click(450, 925, 'left')

        if i % 5 == 2:
            # print("卖怪")
            x = random.randint(450, 1400)
            y = random.randint(700, 800)
            print("卖怪 " + str(x) + " " + str(y))
            auto.mouseDown(x=x, y=y, button='left')
            auto.mouseUp(x=x, y=y+180, button='left', duration=1)

        if i % 5 == 1:
            x = random.randint(500, 1400)
            y = random.randint(900, 1000)
            print("买牌 " + str(x) + " " + str(y))
            on_click(x, y, 'left')

        if i % 5 == 0:
            x = random.randint(800, 1300)
            y = random.randint(200, 700)
            print("走走 " + str(x) + " " + str(y))
            on_click(x, y, 'right')


def room_ok():
    picture = auto.locateOnScreen('assert/okTag.png')
    if picture is not None:
        auto.moveTo(picture)
        auto.click(clicks=2, interval=1)

def game():
    i = 1
    while True:

        room_start()
        if INGAME == 0:
            room_accept()
        room_end()
        room_ok()
        draft_stage('assert/inGame.png')
        draft_stage('assert/inGame.png')
        ff_stage('assert/3-4Tag.png')
        in_game_stage(i)
        i += 1
        print(i)


if __name__ == '__main__':
    time.sleep(5)
    game()
