'''
#########################
# Author : ArshZ0       #
# Created : 03 NOV 2021 #
#########################
'''

import sys

def main():
    args = sys.argv[1:]
    if (len(args)<3):
        print("Missing arguments\n\tpython codec.py <image> <message> <output>")
        exit()
    if (len(args)>3):
        print("Too much arguments\n\tpython codec.py <image> <message> <output>")
        exit()

    print('''
    #############################################################
    #   Steganography - Least Significant Bit Image - ArshZ0    #
    #############################################################\n
    ''')


if __name__ == '__main__' :
    main()