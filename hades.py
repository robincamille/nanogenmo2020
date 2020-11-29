#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Hades generated text

import requests
from random import randint

    
# gather corpora

def getCorp(address,list_title):
    '''Returns list from a JSON-formatted list'''
    response = requests.get(address)
    output = response.json()[list_title]
    return output

def randItem(list_title):
    return list_title[randint(0, len(list_title)-1)]

#greek_gods = getCorp('https://raw.githubusercontent.com/dariusk/corpora/master/data/mythology/greek_gods.json','greek_gods')

greek_monsters = getCorp('https://raw.githubusercontent.com/dariusk/corpora/master/data/mythology/greek_monsters.json','greek_monsters')
general_monsters = getCorp('https://raw.githubusercontent.com/dariusk/corpora/master/data/mythology/monsters.json','names')
monsters = greek_monsters + general_monsters

adjs = getCorp('https://raw.githubusercontent.com/dariusk/corpora/master/data/words/adjs.json','adjs')
nouns = getCorp('https://raw.githubusercontent.com/dariusk/corpora/master/data/words/nouns.json','nouns')

verbs_raw = requests.get('https://raw.githubusercontent.com/dariusk/corpora/master/data/words/verbs_with_conjugations.json')

rarity = ['','','','','Rare ','Epic ','Heroic ','Legendary '] #spaces included
thing_to_affect = ["strikes","damage","dashes","any status effect"]

infile = open('gods.txt','r')
greek_gods = infile.readlines()
infile.close()

infile = open('weapons.txt','r')
weapons = infile.readlines()
infile.close()


# create log



for i in range(1,10):

    boons_list = []
    for j in range(2,randint(2,12)):
        boon = randItem(greek_gods)[:-1] + "'s " + \
               randItem(rarity) + \
               randItem(adjs).capitalize() + " " + \
               randItem(nouns).capitalize() + ": " + \
               verbs_raw.json()[randint(0,633)]["indicative"]["present"][2].capitalize() + \
               " foes, +" + str(randint(1,500)) + " " + randItem(thing_to_affect)
        boons_list.append(boon)
    
    outcome = "\nRun #" + str(i) + \
              "\nRuntime: " + str(randint(1,200)) + ":" + str(randint(10,59)) + \
              "\nKilled by " + randItem(monsters).capitalize() + " in Chamber #" + str(randint(1,61)) + \
              "\nArmed with the " + randItem(weapons)[:-1] + " of " + randItem(greek_gods)[:-1] + \
              "\nBoons:\n  " + "\n  ".join(boons_list)
    print(outcome)
