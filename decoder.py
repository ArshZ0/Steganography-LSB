#########################
# Author : ArshZ0       #
# Created : 03 NOV 2021 #
#########################

import sys
from PIL import Image
import numpy as np
from time import sleep

def int_to_bin(val):
    val = bin(val)[2:]
    while (len(val)<8):
        val = '0'+val
    return val

def main():
    args = sys.argv[1:]
    if (len(args)<2):
        print("Missing arguments\n\tpython codec.py <image> <message> <output>")
        exit()
    if (len(args)>2):
        print("Too many arguments\n\tpython codec.py <image> <message> <output>")
        exit()

    print('''
    #############################################################
    #   Steganography - Least Significant Bit Image - ArshZ0    #
    #############################################################
    ''')

    try: 
        image = Image.open(args[0], "r")
    except:
        print("Error: \'"+args[0]+"\' does not exist")
        exit()

    print("Loading of "+args[0]+" ...\n");sleep(0.5)

    image = image.convert('RGBA')
    pixels = image.load()

    try:
        output = open(args[1], "x+")
    except:
        print("Error: \'"+args[1]+"\' already exist")
        exit()

    print("Writing into "+args[1]+" ...\n");sleep(0.5)

    message = ""

    for y in range(image.size[1]):
        for x in range(image.size[0]):
            r,g,b,a = pixels[x, y]
            r = int_to_bin(r)[-2:]
            g = int_to_bin(g)[-2:]
            b = int_to_bin(b)[-2:]
            a = int_to_bin(a)[-2:]
            rgba = int(r+g+b+a,2)
            if (rgba!=0) :
                message+=chr(rgba)
    
    output.write(message)
    output.close()
    image.close()



if __name__ == '__main__' :
    main()