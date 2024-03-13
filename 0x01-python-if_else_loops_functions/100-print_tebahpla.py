#!/usr/bin/python3
for chara in range(122, 96, -1):
   if chara % 2 != 0:
        chara -= 32
   print("{}".format(chr(chara)), end='')
        
