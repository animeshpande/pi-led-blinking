#! /usr/bin/python
from gpiozero import LED
from time import sleep

count = 0
led1 = LED(15)
led2 = LED(14)
led3 = LED(18)

def toggle_led(led1,led2):
    led1.on()
    sleep(0.005)
    led2.on()
    sleep(0.005)
    led1.off()
    sleep(0.1)

while True: #count < 50:
    toggle_led(led1,led2)
    toggle_led(led2,led3)
    toggle_led(led3,led1    )
    count += 1
