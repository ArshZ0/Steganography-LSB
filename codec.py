#########################
# Author : ArshZ0       #
# Created : 03 NOV 2021 #
#########################

import sys
from PIL import Image
import numpy as np

def main():
    args = sys.argv[1:]
    if (len(args)<3):
        print("Missing arguments\n\tpython codec.py <image> <message> <output>")
        exit()
    if (len(args)>3):
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

    try:
        output = open(args[2], "w+")
    except:
        print("Error: \'"+args[2]+"\' already exist")
        exit()


    image = image.convert('RGBA')
    pixels = image.load()

    for y in range(image.size[1]):
        for x in range(image.size[0]):
            r,g,b,a = pixels[x, y]
            print("RED: ",r,"\tGREEN: ",g,"\tBLUE: ",b, "\tALPHA: ",a)



if __name__ == '__main__' :
    main()