# Steganography - Least Significant Bit

Hide secret message into an image.

**Message Length < Image.size**

## Codec

Execute with python
```bash
python codec.py <image> <message> <output>
```
or with python3
```bash
python3 codec.py <image> <message> <output>
```

## Decoder

Execute with python
```bash
python decoder.py <image> <output>
```
or with python3
```bash
python3 decoder.py <image> <output>
```

## How it works ?

Get color of each pixel from the image in RGBA
```bash
(255, 0, 0, 255) -> red
(0, 255, 0, 255) -> green
(0, 0, 255, 255) -> blue
```
Set the last 2 bits of each color at 0 : 
```bash
255 -> 252
```
Then, transform each character of the message into binary, split them into 4 blocs of 2 bits and put them in the colors
```bash
(252, 0, 0, 252) -> Initial color & 252
a = 97 = 01 10 00 01
(253, 2, 0, 253) -> Color with hidden char
```