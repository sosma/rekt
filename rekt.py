#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import choice
from time import sleep
different = "qwertyuiopasdfgjklzxcvbnm1234567890+!#¤%&/()=?<>|,;.:-_[]/QWERTYUIOPASDFGHJKLZXCVBNM "


while(True):
    sleep(0.01)
    letter0 = choice(different)
    letter1 = choice(different)
    letter2 = choice(different)
    letter3 = choice(different)
    letter4 = choice(different)
    letter5 = choice(different)
    letter6 = choice(different)

    print letter0 + letter1 + letter2 + letter3 + letter4 + letter5 + letter6
    if letter0=="[":
        break
while(True):
    sleep(0.0105)
    letter0 = "["
    letter1 = choice(different)
    letter2 = choice(different)
    letter3 = choice(different)
    letter4 = choice(different)
    letter5 = choice(different)
    letter6 = choice(different)

    print letter0 + letter1 + letter2 + letter3 + letter4 + letter5 + letter6
    if letter1==" ":
        break
while(True):
    sleep(0.011)
    letter0 = "["
    letter1 = " "
    letter2 = choice(different)
    letter3 = choice(different)
    letter4 = choice(different)
    letter5 = choice(different)
    letter6 = choice(different)

    print letter0 + letter1 + letter2 + letter3 + letter4 + letter5 + letter6
    if letter2=="]":
        break
while(True):
    sleep(0.01125)
    letter0 = "["
    letter1 = " "
    letter2 = "]"
    letter3 = choice(different)
    letter4 = choice(different)
    letter5 = choice(different)
    letter6 = choice(different)

    print letter0 + letter1 + letter2 + letter3 + letter4 + letter5 + letter6
    if letter3=="R":
        break
while(True):
    sleep(0.0125)
    letter0 = "["
    letter1 = " "
    letter2 = "]"
    letter3 = "R"
    letter4 = choice(different)
    letter5 = choice(different)
    letter6 = choice(different)

    print letter0 + letter1 + letter2 + letter3 + letter4 + letter5 + letter6
    if letter4=="e":
        break

while(True):
    sleep(0.015)
    letter0 = "["
    letter1 = " "
    letter2 = "]"
    letter3 = "R"
    letter4 = "e"
    letter5 = choice(different)
    letter6 = choice(different)

    print letter0 + letter1 + letter2 + letter3 + letter4 + letter5 + letter6
    if letter5=="k":
        break
while(True):
    sleep(0.02)
    letter0 = "["
    letter1 = " "
    letter2 = "]"
    letter3 = "R"
    letter4 = "e"
    letter5 = "k"
    letter6 = choice(different)

    print letter0 + letter1 + letter2 + letter3 + letter4 + letter5 + letter6
    if letter6=="t":
        break
print "[x]Rekt"
