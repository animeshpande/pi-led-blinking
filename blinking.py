#! /usr/bin/python
from gpiozero import LED
from time import sleep

count = 0
led1 = LED(15)
led2 = LED(14)
led3 = LED(18)

def toggle_led(led):
    sleep(1)
    led.on()
    sleep(0.5)
    led.off

while count < 50:
    toggle_led(led1)
    toggle_led(led2)
    toggle_led(led3)
    count += 1
