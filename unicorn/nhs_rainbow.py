#!/usr/bin/env python

import math
import time
import signal

import unicornhat as unicorn


print("""NHS Logo & Rainbow

Displays the NHS Logo and then a beautiful rainbow across your HAT/pHAT :D

""")

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()


print("Starting to clap....")
time.sleep(.5)
print("Thanks NHS")
time.sleep(.5)
print("Enjoy the rainbows!...")

while True:
    pixels = [[(0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255)], [(0, 0, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255)], [(0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255)], [(0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255)]]
    unicorn.set_pixels(pixels)
    unicorn.show()
    time.sleep(5)


    pixels = [[(0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255)], [(0, 0, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255)], [(0, 0, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255)], [(0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255)]]
    unicorn.set_pixels(pixels)
    unicorn.show()
    time.sleep(5)

    pixels = [[(0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)], [(0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)], [(0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)], [(0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)]]
    unicorn.set_pixels(pixels)
    unicorn.show()
    time.sleep(5)
    
    x = 0
    i = 0.0
    offset = 30
    for x in range (0,500):
        i = i + 0.3
        for y in range(height):
                for x in range(width):
                        r = 0
                        g = 0
                        r = (math.cos((x+i)/2.0) + math.cos((y+i)/2.0)) * 64.0 + 128.0
                        g = (math.sin((x+i)/1.5) + math.sin((y+i)/2.0)) * 64.0 + 128.0
                        b = (math.sin((x+i)/2.0) + math.cos((y+i)/1.5)) * 64.0 + 128.0
                        r = max(0, min(255, r + offset))
                        g = max(0, min(255, g + offset))
                        b = max(0, min(255, b + offset))
                        unicorn.set_pixel(x,y,int(r),int(g),int(b))
        unicorn.show()
        time.sleep(0.01)
        x = x + 1
