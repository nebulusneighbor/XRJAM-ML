
# -*- coding: utf-8 -*-
import time
from pynput. keyboard import Key, Controller

counter=0


while time.time() > 0:

    timer= time.sleep(4)
    keyboard = Controller()
    #key = "enter"

    keyboard. press(Key.enter)
    keyboard. release(Key.enter)
    counter = counter + 1
    print ("number of cycles: ")
    print (counter)
