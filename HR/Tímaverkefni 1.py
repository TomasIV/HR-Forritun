#8/15/2019
#Tómas Ingi Villalobos
#HR

import os

n = (" Nafn         : Tómas Ingi Villalobos\n") # Nafn
h = ("Heimilisfang : Kelduhvammur 11\n") # heimilisfang
s = ("Símanúmer    : 894-7350") # Símanúmer
run = True
while run:
    val = input("\n1. message of the day\n2. buisness card\3. stop\nVelkominn, sláðu inn tölu til að velja lið: ")
    if val == "1":
        print ("\nHello world")
    elif val == "2":
        print ("\n", n, h, s)
    elif val == "3":
        run = False

