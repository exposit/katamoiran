#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# seed.py
#
#
# python seed.py <filename> [-a pos] [-b pos] 
#
# pos can be noun, adjective, verb, adverb
#

import os
import sys

import random
from random import choice

# patterns
patternA = 'verb'
patternB = 'noun'

try:
    filename = sys.argv[1]
except:
    print("Please specify a file name that you've already run seedparser.py on.")
    sys.exit(1)
    
try:
    filename, ext = filename.split('.')
except:
    pass

typeMap = {'adverb' : [], 'adjective' : [], 'noun' : [], 'verb' : []}
modMap = []
modList = []

try:
    for item in typeMap:
        modMap.append(filename + "_" + item)
    
    modMap.sort()
    
    modList = map(__import__, modMap)

except:
    print("Something's gone wrong with the import; are the output files from running seedparser.py in this directory?")
    sys.exit(1)

#print('(pattern \"' + patternA + ' ' + patternB + '\" from ' + filename + ')\n')

typeMap['adjective'] = modList[0].chart
typeMap['adverb'] = modList[1].chart
typeMap['noun'] = modList[2].chart
typeMap['verb'] = modList[3].chart

chartA = typeMap[patternA][0]
chartB = typeMap[patternB][0]

try:
    flag = sys.argv[2]
    pattern = sys.argv[3]
    if flag == '-a':
        for item in typeMap:
            if item.startswith(pattern):
                patternA = item
                chartA = typeMap[item][0]
except:
    pass
    
try:
    flag = sys.argv[4]
    pattern = sys.argv[5]
    if flag == '-b':
        for item in typeMap:
            if item.startswith(pattern):
                patternB = item
                chartB = typeMap[item][0]
except:
    pass

result = 'Seed: \"' + str(choice(chartA)) + ' ' + str(choice(chartB)) + '\"'
print(result)


