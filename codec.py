#########################
# Author : ArshZ0       #
# Created : 03 NOV 2021 #
#########################

import sys
from PIL import Image
import numpy as np
from time import sleep

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

    print("Loading of "+args[0]+" ...\n");sleep(0.5)

    image = image.convert('RGBA')
    pixels = image.load()

    try:
        message_file = open(args[1], "r")
    except:
        print("Error: \'"+args[1]+"\' does not exist")
        exit()

    print("Reading of "+args[1]+" ...\n");sleep(0.5)

    message_lines = message_file.readlines()
    message = ""
    for i in message_lines:
        message+=i
    print(message)

    if (len(message)>image.size[0]*image.size[1]):
        print("Error: Message too long for the size of the image")
        exit()

    try:
        output = open(args[2], "x+")
    except:
        print("Error: \'"+args[2]+"\' already exist")
        exit()

    print("Creating of "+args[2]+" ...\n");sleep(0.5)

    out = Image.new('RGBA', image.size)
    out_pixels = out.load()

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
                curr_char+=1
            out_pixels[x, y] = (r, g, b, a)
    out.save(args[2])

    image.close()
    message_file.close()
    output.close()

if __name__ == '__main__' :
    main()