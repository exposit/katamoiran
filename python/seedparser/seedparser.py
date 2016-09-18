#
#  Seed List Parser
#
#  Simple script to take text from a plain text file, sort it into rough parts of speech, and
# then save it as python lists and csv-formatted dXX charts for use in seeding 
#
#	Usage:
#
#		python seedparser.py <filename>
#
#	Flags:
#
#	    -m, --max	integer
#	    	Max number of elements in final lists. Set higher than target so you have extras for curated lists.
#
#	    -f, --fill	True or False
#		    Keep trying until the list is full (max 3x limiter), default is True
#
#	    -c, --case	u[pper] or l[ower
#	    	Results in title case or lowercase, default is lowercase
#
#	    -l, --lemmatize	True or False
#	    	Convert verbs to base form, default is True
#
#	    -p, --print	True or False
#	    	Print results to terminal, default is False
#


import nltk
from nltk import *
from nltk.stem.wordnet import WordNetLemmatizer

import os
import sys
import string

import random
from random import sample

# declare defaults here
limiter = 100
repeat = True
case = 'lower'
lemmatize_verbs = True
print_to_terminal = False

try:
    filename = sys.argv[1]
except:
    print("\tUsage:\n\t\tpython seedparser.py <filename>")
    print("\tFlags:")
    print("\t-m, --max\tnumber\n\t\tMax number of elements in final lists. Set higher than target so you have extras for curated lists.")
    print("\t-f, --fill\tTrue or False\n\t\tKeep trying until the list is full (max 3x limiter), default is True")
    print("\t-c, --case\tu[pper] or l[ower\n\t\tResults in title case or lowercase, default is lowercase")
    print("\t-l, --lemmatize\tTrue or False\n\t\tConvert verbs to base form, default is True")
    print("\t-p, --print\tTrue or False\n\t\tPrint results to terminal, default is False")
    sys.exit(1)

para_string = filename

try:
    for i in range(1, len(sys.argv)):
        flag = sys.argv[i]
        parameter = sys.argv[i+1]
        if flag == '-f' or flag == '--fill':
            if parameter == 'False':
                repeat = False
            para_string = para_string + ", fill: " + str(repeat)
        elif flag == '-c' or flag == '--case':
            if parameter == 'upper' or parameter == 'lower' or parameter == 'u' or parameter == 'l':
                case = parameter
            para_string = para_string + ", case: " + str(case)
        elif flag == '-l' or flag == '--lemmatize':
            if parameter == 'False':
                lemmatize_verbs = False
            para_string = para_string + ", lemmatize: " + str(lemmatize_verbs)
        elif flag == '-p' or flag == '--print':
            if parameter == 'True':
                print_to_terminal = True
            para_string = para_string + ", print to terminal: " + str(print_to_terminal)
        elif flag == '-m' or flag == '--max':
            limiter = int(parameter)
            para_string = para_string + ", max elements: " + str(limiter)
except:  
    pass

if print_to_terminal == True:
    print(para_string)
    
# first, set up lists
def parseFile(filename):

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
                # convert to base form of the verb if possible
                if lemmatize_verbs == True:
                    word = WordNetLemmatizer().lemmatize(word,'v')
                verbs.append(word)
            if pos == 'NN' or pos == 'NNS':
                nouns.append(word)
            if pos.startswith('RB'):
                adverbs.append(word)

    return [adverbs, adjectives, nouns, verbs]

# now do some processing on the words and save things
def processList(posList, limiter, wordtype, filename):

    nameList=["adverb", "adjective", "noun", "verb"]
    name = nameList[wordtype]
    
    try:
        filename, ext = filename.split('.')
    except:
        pass
    
    # standardize as lower case
    for i in range(len(posList)):
        if case == 'upper':
            posList[i] = string.capwords(posList[i])
        else:
            posList[i] = posList[i].lower()
    
    # remove any duplicates
    posList = list(set(posList))

    tries = 0
    length = 0
    max_tries_exceeded = False
    while length < limiter and max_tries_exceeded == False:
        tries = tries + 1
        try:
            posList = sample(posList, limiter)
        except:
            #del posList[limiter:]
            pass
            
        length = len(posList)

        if tries > limiter*10:
            max_tries_exceeded = True
            
    posList.sort()

    # print for using in python script
    format_py = '\n\'' + name + '\' : [\"' + '\", \"'.join(posList).replace('\n','') + "\"],"
    
    if print_to_terminal == True:
        print(format_py)

    # and save it
    with open("." + os.sep + filename + "_" + name + ".py", 'w') as f:
        f.write(format_py)

    # print as d100 table in comma-separated list
    format_csv = ""
    count = 0
    
    result = "\n" + name + " [" + str(len(posList)) + "]:\n"
    
    for i in range(len(posList)):
        count = count + 1
        result = result + str(count) + ", " + posList[i].rstrip()
        if count % 5 == 0:
            result = result + "\n     "
        else:
            result = result + ", , "

    format_csv = result
    
    if print_to_terminal == True:
        print(format_csv)
    
    if print_to_terminal == True:
        print(name + " [" + str(len(posList)) + "]" )
    
    # and save it
    with open("." + os.sep + filename + "_" + name + ".csv", 'w') as f:
        f.write(format_csv)

typeList = parseFile(filename)

for i in range(len(typeList)):
    length = 0
    wordList = typeList[i]
    processList(wordList, limiter, i, filename)
    
    
