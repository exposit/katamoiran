# -*- coding: utf-8 -*-

import random
import glob
import os
import sys
import string
import time

# -f <letters> to use those as the first letters
# -n <number> to make that many names (default 10)
# -l to limit names to a maximum length (default is equal to the longest source word)
# -m <number> will set a minimum name length (default is 3)
# -d <n,n,n> to specify datafiles and skip input prompt
# -k <word or phrase> will only grab files containing that word in the name. Note that 'male' would
# normally match 'female' or 'male' but I've given it a special clause.

# logging variables
#start_time = time.time()

# declare defaults here
limiter = -99
names_to_make = 10
first_letters = ""
fileindex = ""
keyword = ""
minimum = 3
exit = False

# parse any flags
try:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("-f <letters> to use those as the first letters")
        print("-n <number> to make that many names (default 10)")
        print("-l to limit names to a maximum length (default is equal to the longest source word)")
        print("-m <number> will set a minimum name length (default is 3)")
        print("-d <n,n,n> to specify datafiles and skip input prompt")
        print("-k <string> will grab files with that string in the name.")
        exit = True
except:
    pass

if exit != False:
    sys.exit(1)

try:
    for i in range(1, len(sys.argv)-1):
        flag = sys.argv[i]
        parameter = sys.argv[i+1]
        if flag == '-f' or flag == '--first':
            if len(parameter) > 0:
                first_letters = parameter
        elif flag == '-n' or flag == '--number':
            names_to_make = int(parameter)
        elif flag == '-l' or flag == '--length' or flag == '--max':
            limiter = int(parameter)
        elif flag == '-d' or flag == '--datafiles':
            fileindex = ','.join(parameter.split(','))
        elif flag == '-k' or flag == '--keyword':
            keyword = parameter
        elif flag == '-m' or flag == '--minimum' or flag == '--min':
            minimum = int(parameter)
except:
    pass

DATAFILE = []
NAMELIST = []
RESULTLIST = []

#dfiles = glob.glob("." + os.sep + "data" + os.sep + "*")
#print(dfiles)

dfiles = []
dirlist = []
for root, dirs, files in os.walk("." + os.sep + "data" + os.sep):
    for file in files:
        if file.endswith(".txt"):
            dirlist.append(root.split(os.sep)[-1])
            dfiles.append(os.path.join(root, file))

print("\n")

if len(keyword) > 0:
    if keyword == "male":
        keyword = " male"
    fileindex = ','.join([str(dfiles.index(x)) for x in dfiles if keyword in x])

if len(fileindex) == 0:

    prettyList = []
    count = 0
    for i in range(len(dfiles)):
        tag = " "
        if len(dirlist[i]) > 0:
            tag = "(" + dirlist[i][:5] + ") "
        prettyList.append(tag + dfiles[i].split(os.sep)[-1][:-4].replace('_', " "))
        count = count + 1

    breaker = 2
    count = 0
    for i in range(0, len(prettyList), breaker):
        print("%-2s %-3d %30s %-3s %-3d %25s" % (" ", count, prettyList[count], " ", count+1, prettyList[count+1]))
        count = count + 2

    fileindex = raw_input("\nSources? (Separate with a comma, no space.) ")

fileList = fileindex.split(',')

# now open that save file
for index in fileList:
    with open(dfiles[int(index)], 'r') as infile:
        data = infile.read()
    DATAFILE = DATAFILE + data.split(", ")
    DATAFILE = [x.strip('\n') for x in DATAFILE]
    DATAFILE = [x.strip('\t') for x in DATAFILE]
    NAMELIST.append(dfiles[int(index)].split(os.sep)[-1][:-4])

if limiter <= 0:
    for element in DATAFILE:
        #print(limiter, element, len(element))
        limiter = max(limiter, len(element))

###############################################################################
# Markov Name model
# A random name generator, by Peter Corbett
# http://www.pick.ucam.org/~ptc24/mchain.html
# This script is hereby entered into the public domain
###############################################################################
class Mdict:
    def __init__(self):
        self.d = {}
    def __getitem__(self, key):
        if key in self.d:
            return self.d[key]
        else:
            raise KeyError(key)
    def add_key(self, prefix, suffix):
        if prefix in self.d:
            self.d[prefix].append(suffix)
        else:
            self.d[prefix] = [suffix]
    def get_suffix(self,prefix):
        l = self[prefix]
        return random.choice(l)

class MName:
    """
    A name from a Markov chain
    """
    def __init__(self, chainlen = 2):
        """
        Building the dictionary
        """
        if chainlen > limiter or chainlen < 1:
            print "Chain length must be between 1 and " + limiter + ", inclusive"
            sys.exit(0)

        self.mcd = Mdict()
        oldnames = []
        self.chainlen = chainlen

        for l in DATAFILE:
            l = l.strip()
            oldnames.append(l)
            s = " " * chainlen + l
            for n in range(0,len(l)):
                self.mcd.add_key(s[n:n+chainlen], s[n+chainlen])
            self.mcd.add_key(s[len(l):len(l)+chainlen], "\n")

    def New(self):
        """
        New name from the Markov chain
        """
        prefix = " " * self.chainlen
        name = ""
        if len(first_letters) > 0:
            name = first_letters
        suffix = ""
        while True:
            suffix = self.mcd.get_suffix(prefix)
            if suffix == "\n" or len(name) > limiter:
                break
            else:
                name = name + suffix
                prefix = prefix[1:] + suffix
        return name.title()

# End public domain bit
# And some more print prettifying
tries = 0
max_tries = 1000
while len(RESULTLIST) < names_to_make and tries <= max_tries:
    possible = MName().New()
    if len(possible) >= minimum:
        RESULTLIST.append(possible)
    tries = tries + 1

if len(RESULTLIST) < names_to_make:
    print("\nI couldn't make all the names you wanted at that length (" + str(minimum) + "). Please select more source files or try a different minimum length.\n")

if len(RESULTLIST) > 0:
    print("\nSources: " + ', '.join(NAMELIST))
    print("\nMinimum length: " + str(minimum))

    print("\n************************\n")
    print(', '.join(RESULTLIST))
    print(" ")
    print("\n************************\n")
