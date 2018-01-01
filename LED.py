from RPi.GPIO import GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class LED:
    def __init__(self):
        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(9, GPIO.OUT)
        GPIO.setup(10, GPIO.OUT)
        GPIO.setup(25, GPIO.OUT)
        GPIO.setup(8, GPIO.OUT)

    def change_num(self, num):
        num = num - 1
        num = num % 6 + 1
        if num == 1:
            return 7
        if num == 2:
            return 11
        if num == 3:
            return 9
        if num == 4:
            return 10
        if num == 5:
            return 25
        if num == 6:
            return 8

    def turn_on(self, num):
        GPIO.output(self.change_num(num), GPIO.HIGH)

    def turn_off(self, num):
        GPIO.output(self.change_num(num), GPIO.LOW)


led = LED()
while True:
    for j in range(1, 5):
        for i in range(j, j + 6):
            led.turn_on(i)
            time.sleep(0.5)
            led.turn_off(i - j + 1)
        led.turn_on(j)
        time.sleep(0.5)
    led.turn_on(6)
    time.sleep(0.5)
    for i in range(1, 7):
        led.turn_off(i)