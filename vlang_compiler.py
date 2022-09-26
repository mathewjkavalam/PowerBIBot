"""
REPL for Visual "V" Language

"""

from ast import arg
from place_visual import function1

debug = False
vlang_opwords = ["CDX","`"]
tokens = {}
quit = False

i = 0
while not quit:
    cleaned = []
    in_word = input("vlang>")
    if debug: print(in_word)
    opword = in_word[0:3]
    if opword == '`': quit = True
    if opword in vlang_opwords and not quit:
        i += 1
        args = in_word[3:]
        if debug:print(in_word)
        args = args.split(',')
        if debug:print(args)
        for each in args:
            each = each.strip()
            if debug: print(each)
            cleaned.append(each)
        tokens[i] = {"op":opword,"args":cleaned}
        if debug:tokens
        if opword == 'CDX':
            function1(args[0],args[1],args[2],args[3],args[4])
    else:
        print("Not a recognised keywords:"+in_word)
    if debug: print(tokens)
