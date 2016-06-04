#!/usr/bin/python
# -*- encoding: utf-8 -*-

import random
import gettext
from datetime import datetime
import argparse


try:
    input = raw_input
except NameError:
    pass

def keyboardinput(txt):

    kbpinputok = False
    while not kbpinputok:
        kbdinput = input(txt)
        try:
            if int(kbdinput) >= 0 and int(kbdinput) <= 100:
                kbpinputok = True
        except:
            if kbdinput == 'fin':
                kbpinputok = True
            else:
                pass
    return kbdinput


def _(s):

    return s

def startmessage(prenom):
    print (_('Salut %s, c\'est partie' % (prenom)))


def multiplication(tbl):

    min = tbl
    max = tbl
    
    if tbl == -1:
        min = 0
        max = 10

    facteur1 = random.randint(min, max)
    facteur2 = random.randint(0, 10)
    produit = facteur1*facteur2

    return facteur1, facteur2, produit

def resultat(equations, nbbonnereponse, nboperation):
    print (_('--------------- Resultats Complet ---------------'))
    for equation in equations:
        print(equation)
    try:
        note = ('%s/20' % str(nbbonnereponse*20/nboperation))
    except:
        note = _('non noté')

    print('')
    print(_('=> tu as reussis %s multiplications sur %s (%s)') % (str(nbbonnereponse), str(nboperation), note))
    print(_('-------------------------------------------------'))

def start(prenom, table):

    nbbonnereponse = 0
    nboperation = 0

    bonnereponse = ['C\'est bien %s' % prenom, 'Bravo %s' % prenom, 'Bien %s, continue' % prenom, 'C\'est super %s' % prenom]
    mauvaisereponse = ['C\'est pas correct %s' % prenom, 'C\'est mauvais %s' % prenom]

    equations = []
    
    while True:

        facteur1, facteur2, produit = multiplication(table)
        
        txt = str(facteur1) +' X ' + str(facteur2) + ' = '
        timestart = datetime.now()
        res = keyboardinput(txt)

        if res == _('fin'):
            resultat(equations, nbbonnereponse, nboperation)
            exit()
        else:
            if int(res) == produit:
                nbbonnereponse = nbbonnereponse+1
                reponse = bonnereponse[random.randint(0, len(bonnereponse)-1)]
            else:
                reponse = _('%s, ça fait %i') % (mauvaisereponse[random.randint(0, len(mauvaisereponse)-1)], produit)
            reponse = ('%s (%ss)' %(reponse, (datetime.now()-timestart).seconds))
            equations.append('%s %s => %s' % (txt, res, reponse))
            nboperation = nboperation+1
            print(reponse)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=_('Reviewing multiplication tables for children.'))
    parser.add_argument('--version', action='version', version='%(prog)s 0.10')
    parser.add_argument('-f', action='store', dest='childname', help=_('prenom'), default='')
    parser.add_argument('-t', action='store', dest='table', type=int, help=_('multiplication table'), default=-1)
    results = parser.parse_args()
    
    childname = results.childname
    table = results.table
    
    startmessage(childname)
    start(childname, table)

