from machine import Pin  # type: ignore # Pinモジュールをインポート
import time  # timeモジュールをインポート

# 各LEDを制御するPinオブジェクトを作成
led12 = Pin(12, Pin.OUT)
led13 = Pin(13, Pin.OUT)
led14 = Pin(14, Pin.OUT)
led15 = Pin(15, Pin.OUT)
led16 = Pin(16, Pin.OUT)
led17 = Pin(17, Pin.OUT)
led18 = Pin(18, Pin.OUT)
led19 = Pin(19, Pin.OUT)


# すべてのLEDを消灯する関数
def reset():
    led12.low()
    led13.low()
    led14.low()
    led15.low()
    led16.low()
    led17.low()
    led18.low()
    led19.low()


# 数字ごとのLEDパターンを設定する関数
def zero():
    led12.high()
    led13.high()
    led14.high()
    led16.high()
    led17.high()
    led18.high()


def one():
    led16.high()
    led14.high()


def two():
    led17.high()
    led16.high()
    led19.high()
    led12.high()
    led13.high()


def three():
    led17.high()
    led16.high()
    led19.high()
    led14.high()
    led13.high()


def four():
    led18.high()
    led19.high()
    led16.high()
    led14.high()


def five():
    led17.high()
    led18.high()
    led19.high()
    led14.high()
    led13.high()


def six():
    led17.high()
    led18.high()
    led19.high()
    led12.high()
    led13.high()
    led14.high()


def seven():
    led18.high()
    led17.high()
    led16.high()
    led14.high()


def eight():
    led12.high()
    led13.high()
    led14.high()
    led16.high()
    led17.high()
    led18.high()
    led19.high()


def nine():
    led13.high()
    led14.high()
    led16.high()
    led17.high()
    led18.high()
    led19.high()


# 数字を順番に表示するメインループ
while True:
    # 0から9までの数字を順番に表示
    for num in range(10):
        reset()  # まずすべてのLEDを消灯
        if num == 0:
            zero()
        elif num == 1:
            one()
        elif num == 2:
            two()
        elif num == 3:
            three()
        elif num == 4:
            four()
        elif num == 5:
            five()
        elif num == 6:
            six()
        elif num == 7:
            seven()
        elif num == 8:
            eight()
        elif num == 9:
            nine()
        time.sleep(1)  # 1秒待機
        reset()  # 数字の表示後にすべてのLEDを消灯
        time.sleep(0.5)  # 0.5秒待機してから次の数字を表示

    # 9から0までの数字を逆順に表示
    for num in range(9, -1, -1):
        reset()  # まずすべてのLEDを消灯
        if num == 0:
            zero()
        elif num == 1:
            one()
        elif num == 2:
            two()
        elif num == 3:
            three()
        elif num == 4:
            four()
        elif num == 5:
            five()
        elif num == 6:
            six()
        elif num == 7:
            seven()
        elif num == 8:
            eight()
        elif num == 9:
            nine()
        time.sleep(1)  # 1秒待機
        reset()  # 数字の表示後にすべてのLEDを消灯
        time.sleep(0.5)  # 0.5秒待機してから次の数字を表示
