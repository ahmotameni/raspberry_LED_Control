# from RPi.GPIO import GPIO
import time


# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)


class LED:
    def __init__(self, gpio_number):
        self.gpio_number = gpio_number
        # GPIO.setup(gpio_number, GPIO.OUT)

    def turn_on(self):
        print("on")
        # GPIO.output(self.gpio_number, GPIO.HIGH)

    def turn_off(self):
        print("Off")
        # GPIO.output(self.gpio_number, GPIO.LOW)


led_list = [LED(7), LED(11)]
# led_list.append(LED(7))
# led_list.append(LED(11))
# led_list.append(LED(9))
# led_list.append(LED(10))
# led_list.append(LED(25))
# led_list.append(LED(8))

led_list[0].turn_on
