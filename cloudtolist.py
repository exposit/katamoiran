#
#
#  Simple script to take a word list or text file, sort it into rough parts of speech, and
# then save it as a python lists and csv-formatted dXX chart.
#
# Usage is 'python cloudtolist <filename> <limiter>'
#


import nltk
from nltk import *
from nltk.stem.wordnet import WordNetLemmatizer

import os
import sys
import random
from random import sample

# declare filename Here

filename = 'one_chunk.txt'
limiter = 100

try:
    filename = sys.argv[1]
    limiter = int(sys.argv[2])
except:
    pass

def parseFile(filename, limiter):

        words = []
        lines = []

        with open("." + os.sep + filename, 'r') as f:
            lines = f.readlines()

        wordcount = 0

        adverbs = []
        adjectives = []
        nouns = []
        verbs = []

        postuples = word_tokenize(' '.join(lines))
        postuples = nltk.pos_tag(postuples)

        for word, pos in postuples:
            if len(word) > 3:
                if pos.startswith('J'):
                    adjectives.append(word)
                if pos.startswith('V'):
                    newword = WordNetLemmatizer().lemmatize(word,'v')
                    verbs.append(newword)
                if pos == 'NN' or pos == 'NNS':
                    nouns.append(word)
                if pos.startswith('RB'):
                    adverbs.append(word)

        typeList = [adverbs, adjectives, nouns, verbs]
        nameList=["adverb", "adjective", "noun", "verb"]

        # now do some processing on the words
        for x in range(len(typeList)):
            posList = typeList[x]
            for i in range(len(posList)):
                posList[i] = posList[i].lower()

            try:
                posList = sample(posList, limiter)
            except:
                del posList[limiter:]

            posList = list(set(posList))
            posList.sort()
            typeList[x] = posList

        # print for using in python script
        full_py = ""
        for i in range(len(typeList)):

            posList = typeList[i]

            full_py = full_py + '\n\'' + nameList[i] + '\' : [\"' + '\", \"'.join(posList).replace('\n','') + "\"],"

        print(full_py)
        format_py = full_py

        with open("." + os.sep + filename + ".py", 'w') as f:
            f.write(format_py)

        # print as d100 table, csv
        full_csv = ""
        for x in range(len(typeList)):
            count = 0
            result = "\n" + nameList[x] + "[" + str(len(typeList[x])) + "]:\n"
            chart = typeList[x]
            for i in range(len(chart)):
                count = count + 1
                result = result + str(count) + ", " + chart[i].rstrip()
                if count % 5 == 0:
                    result = result + "\n     "
                else:
                    result = result + ", , "

            full_csv = full_csv + result

        print(full_csv)
        format_csv = full_csv

        with open("." + os.sep + filename + ".csv", 'w') as f:
            f.write(format_csv)

parseFile(filename, limiter)
