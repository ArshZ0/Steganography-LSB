#########################
# Author : ArshZ0       #
# Created : 03 NOV 2021 #
#########################

import sys
from PIL import Image
import numpy as np

def split_binary(binary):
    return [binary[i:i+2] for i in range(0, len(binary), 2)]

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
        message_file = open(args[1], "r")
    except:
        print("Error: \'"+args[1]+"\' does not exist")
        exit()

    try:
        output = open(args[2], "x+")
    except:
        print("Error: \'"+args[2]+"\' already exist")
        exit()


    image = image.convert('RGBA')
    pixels = image.load()

    message = message_file.readline()
    curr_char = 0
    length_mess = len(message)-1
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            r,g,b,a = pixels[x, y]
            r = r & 252
            g = g & 252
            b = b & 252
            a = a & 252

            if (curr_char < length_mess):
                binary = bin(ord(message[curr_char]))[2:]
                while (len(binary)<8):
                    binary = '0'+binary
                split = split_binary(binary)
                r+=int(split[0],2)
                g+=int(split[1],2)
                b+=int(split[2],2)
                a+=int(split[3],2)
                #print(message[curr_char],ord(message[curr_char]),binary, split)
                curr_char+=1
            print("RED: ",r,"\tGREEN: ",g,"\tBLUE: ",b, "\tALPHA: ",a)


if __name__ == '__main__' :
    main()