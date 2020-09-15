import time
import pyautogui as auto
import random



TIMES = 0

def game(i):

    picture = auto.locateOnScreen('roomStartTag.bmp')
    if picture is not None:
        print("点击寻找对局")
        auto.moveTo(picture)
        auto.click(clicks=2, interval=1)

    auto.mouseDown(x=952, y=715, button='left')
    auto.mouseUp(x=952, y=715, button='left', duration=1)
    auto.mouseDown(x=952, y=715, button='left')
    auto.mouseUp(x=952, y=715, button='left', duration=1)

    picture = auto.locateOnScreen('1-1Tag.bmp')
    if picture is not None:
        x = random.randint(800, 1300)
        y = random.randint(200, 700)
        print("走走 " + str(x) + " " + str(y))
        auto.mouseDown(x=x, y=y, button='right')
        auto.mouseUp(x=x, y=y, button='right', duration=1)

    picture = auto.locateOnScreen('2-4Tag.bmp')
    if picture is not None:
        x = random.randint(800, 1300)
        y = random.randint(200, 700)
        print("走走 " + str(x) + " " + str(y))
        auto.mouseDown(x=x, y=y, button='right')
        auto.mouseUp(x=x, y=y, button='right', duration=1)


    picture = auto.locateOnScreen('roomEndTag.bmp')
    if picture is not None:
        print("点击再来一盘")
        auto.moveTo(picture)
        auto.click(clicks=2, interval=1)
        global TIMES
        TIMES += 1
        print("已完成-----------" + str(TIMES))






    picture = auto.locateOnScreen('3-4Tag.bmp')
    if picture is not None:
        print("准备认输")
        auto.mouseDown(x=1902, y=851, button='left')
        auto.mouseUp(x=1902, y=851, button='left', duration=1)
        auto.mouseDown(x=1902, y=851, button='left')
        auto.mouseUp(x=1902, y=851, button='left', duration=1)
        time.sleep(2)
        auto.mouseDown(x=759, y=856, button='left')
        auto.mouseUp(x=759, y=856, button='left', duration=1)
        auto.mouseDown(x=759, y=856, button='left')
        auto.mouseUp(x=759, y=856, button='left', duration=1)
        time.sleep(2)
        auto.mouseDown(x=856, y=476, button='left')
        auto.mouseUp(x=856, y=476, button='left', duration=1)
        auto.mouseDown(x=856, y=476, button='left')
        auto.mouseUp(x=856, y=476, button='left', duration=1)
        time.sleep(2)




    picture = auto.locateOnScreen('inGameTag.bmp')
    if picture is not None:

        if i % 5 == 3:
            print("升级")
            auto.press('f')
            time.sleep(1)

        if i % 5 == 2:
            # print("卖怪")
            x = random.randint(450, 1400)
            y = random.randint(700, 800)
            print("卖怪 " + str(x) + " " + str(y))
            auto.moveTo(x, y, tween=auto.linear)
            auto.mouseDown(x=x, y=y, button='left')
            auto.mouseUp(x=x, y=y+160, button='left', duration=1)
            time.sleep(1)


        if i % 5 == 1:

            x = random.randint(500, 1400)
            y = random.randint(900, 1000)
            print("买牌 " + str(x) + " " + str(y))
            auto.moveTo(x, y)
            time.sleep(1)
            auto.mouseDown(x=x, y=y, button='left')
            auto.mouseUp(x=x, y=y, button='left', duration=1)
            time.sleep(1)

        if i % 5 == 0:

            x = random.randint(800, 1300)
            y = random.randint(200, 700)
            print("走走 " + str(x) + " " + str(y))
            auto.moveTo(x, y)
            time.sleep(1)
            auto.mouseDown(x=x, y=y, button='right')
            auto.mouseUp(x=x, y=y, button='right', duration=1)
            time.sleep(1)

        if i % 300 == 0:
            weapons = [(340, 751), (379, 725), (357, 695), (395, 666), (445, 666), (376, 642), (427, 642), (477, 642), (384, 608), (435, 604)]
            chesses = [(962, 668), (915, 563), (960, 497), (1019, 577), (1085, 653), (1127,569), (1073, 509), (1208, 644)]
            for weapon in weapons:
                for chess in chesses:
                    auto.mouseDown(x=weapon[0], y=weapon[1], button='left')
                    auto.mouseUp(x=chess[0], y=chess[1], button='left',duration=0.5)


    return

if __name__ == "__main__":
    i = 1
    while True:
        game(i)
        i += 1
        print(i)
