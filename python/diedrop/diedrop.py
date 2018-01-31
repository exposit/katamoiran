#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Now you don't need physical dice to do a die drop.
#
# dice are public domain from https://openclipart.org/detail/210817/polyhedral-rpg-gaming-dice-dec-2014
#
import os
from glob import glob
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random
import argparse

fontface = "MartelSans-Black.ttf" # change this to whatever font you drop into the fonts directory

parser = argparse.ArgumentParser(description='Drop some dice.')

# this used to make more sense as a list with multiple elements
argmap = {
  'd2' : [2],
  'd4' : [4],
  'd6' : [6],
  'd8' : [8],
  'd10' : [10],
  'd12' : [12],
  'd20' : [20],
}

for key,value in argmap.iteritems():
    parser.add_argument('--' + key, type=int,
                   help='add this many ' + str(value[0]) + '-sided dice')

parser.add_argument('--rotate', '-r', nargs='?', const=1, type=int, default=1, help="rotate the dice; default is 1 (yes)", metavar="0 or 1")

parser.add_argument('--show', '-s', nargs='?', const=1, type=int, default=1, help="open the final image; default is 1 (yes)", metavar="0 or 1")

args = parser.parse_args()

EMPTY = "X"

tmap = [
[EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
[EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
[EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
[EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
[EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
[EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
[EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
[EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
[EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
[EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
]

def assignDice(tmap, size, count):

    for i in range(0,count):

        result = random.randint(1,size)

        x = random.randint(0, len(tmap)-1)
        y = random.randint(0, len(tmap[x])-1)

        iterations = 0
        while tmap[x][y] != EMPTY and iterations <= 1000:
            x = random.randint(0, len(tmap)-1)
            y = random.randint(0, len(tmap[x])-1)
            iterations += 1

        if iterations > 1000:
            print("Oops, couldn't place all dice. Some must have fallen on the floor.")

        img = Image.new('RGBA', (64, 64), 'black')
        draw = ImageDraw.Draw(img)

        choice = "resources" + os.sep + "d" + str(size) + ".png"

        im = Image.open(choice).convert('RGBA')
        im.thumbnail((64,64))
        img.paste(im, (0,0))

        fontpath = os.sep + "font" + os.sep + fontface

        if size <= 10:
            if size == 10 and result == 10:
                result = 0
            font = ImageFont.truetype(fontpath, 34)
            w = 20
            h = 0
        else:
            font = ImageFont.truetype(fontpath, 34)
            if result >=10:
                w = 5
                h = 5
            else:
                w = 18
                h = 5

        draw.text((w,h), str(result), fill=(0,0,0), font=font)

        if args.rotate == 1:
            img = img.rotate(random.randint(0,360), expand=1)

        tmap[x][y] = img

for arg in vars(args):

    value = getattr(args, arg)

    if value != None and arg != "rotate" and arg != "show":
        size = argmap[str(arg)][0]
        count = getattr(args, arg)

        assignDice(tmap, size, count)

new_im = Image.new('RGB', (1500, 1500), 'black')

y_offset = 0
x_offset = 0
rowheight = 0
rowwidth = 0
maxheight = 0
maxwidth = 0
for line in tmap:
    if x_offset > maxwidth:
        maxwidth = x_offset
    x_offset = 0
    for item in line:
        if item == EMPTY:
            img = Image.new('RGB', (64, 64), 'black')
        else:
            img = item

        new_im.paste(img, (x_offset,y_offset))
        x_offset += img.size[0]
        if img.size[1] > rowheight:
            rowheight = img.size[1]
        if img.size[0] > rowwidth:
            rowwidth = img.size[0]

    y_offset += rowheight
    if y_offset > maxheight:
        maxheight = y_offset

new_im = new_im.crop((0, 0, maxwidth, maxheight))

# now let's resize it
old_size = new_im.size

new_size = (old_size[0]+150, old_size[1]+150)
final_im = Image.new("RGB", new_size)
final_im.paste(new_im, ((new_size[0]-old_size[0])/2,
                      (new_size[1]-old_size[1])/2))

existing = glob('output' + os.sep + '*.png')

if len(existing) > 0:
    highest = max(existing)
    count = int(highest.split('.')[0].split('_')[1]) + 1
else:
    count = 1

fname = 'output' + os.sep + 'image_' + str(count).zfill(2) + '.png'
final_im.save(fname)

if args.show == 1:
    os.system('open ' + fname)
    #final_im.show()
