#!/usr/bin/python
# -*- encoding: utf-8 -*-

import random
from datetime import datetime
import argparse


def Keyboardinput(txt):

    kbpInputOk = False
    while not kbpInputOk:
        kbd = raw_input(txt)
        try:
            if int(kbd) >= 0 and int(kbd) <= 100:
                kbpInputOk = True
        except:
            if kbd == 'fin':
                kbpInputOk = True
    return kbd


def Startmessage(prenom):
    print ('Salut %s, c\'est partie' % (prenom))

def Start(prenom):

    nbbonnereponse = 0
    nboperation = 0

    bonnereponse = ['C\'est bien %s' % prenom, 'Bravo %s' % prenom, 'Bien %s, continue' % prenom, 'C\'est super %s' % prenom]
    mauvaisereponse = ['C\'est pas correct %s' % prenom, 'C\'est mauvais %s' % prenom]

    equations = []

    while True:
        facteur1 = random.randint(0, 10)
        facteur2 = random.randint(0, 10)
        produit = facteur1*facteur2
        txt = str(facteur1) +' X ' + str(facteur2) + ' = '
        timestart = datetime.now()
        res = Keyboardinput(txt)

        if res == 'fin':
            print ('--------------- Resultats Complet ---------------')
            for equation in equations:
                print equation
            print ('')
            print ('=> tu as reussis %s multiplications sur %s' % (str(nbbonnereponse), str(nboperation)))
            print ('-------------------------------------------------')
            exit()
        else:
            if int(res) == produit:
                nbbonnereponse = nbbonnereponse+1
                reponse = bonnereponse[random.randint(0, len(bonnereponse)-1)]
            else:
                reponse = '%s, ça fait %i' % (mauvaisereponse[random.randint(0, len(mauvaisereponse)-1)], produit)
            reponse = ('%s (%ss)' %(reponse, (datetime.now()-timestart).seconds))
            equations.append('%s %s => %s' % (txt, res, reponse))
            nboperation = nboperation+1
            print (reponse)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Reviewing multiplication tables for children.', version='0.10')
    parser.add_argument('-f', action='store', dest='firstname', help='firstname of the children', default='firstname')
    results = parser.parse_args()
    
    firstname = results.firstname

    Startmessage(firstname)
    Start(firstname)

