#!/usr/bin/python
# -*- encoding: utf-8 -*-

import random
from datetime import datetime
import argparse


def KeyboardInput(txt):

    kbpInputOk = False
    while not kbpInputOk:
        kbd = raw_input(txt)
        try:
            if int(kbd) >=0 and int(kbd) <= 100:
                kbpInputOk=True
        except:
            if kbd == 'fin':
                kbpInputOk = True
    return kbd


def StartMessage(prenom):
    print ('Salut %s, c\'est partie' % (prenom))

def Start(prenom):

    nbbon=0
    nb=0

    bonnereponse=['C\'est bien %s' % prenom,'Bravo %s' % prenom, 'Bien %s, continue' % prenom,'C\'est super']
    mauvaisereponse=['C\'est pas correct %s' % prenom, 'C\'est mauvais %s' % prenom]

    equations=[]

    while True:
        
        a=random.randint(0, 10)
        b=random.randint(0, 10)
        valid=a*b
        txt = str(a) +' X ' + str(b) + ' = '
        ts = datetime.now()
        
        res=KeyboardInput(txt)

        if res=='fin':
            print ('--------------- Resultats Complet ---------------')
            for equation in equations:
                print equation
            print ('')
            print ('=> tu as reussis %s multiplications sur %s' % (str(nbbon),str(nb)))
            print ('-------------------------------------------------')
            exit()
        else:
            if int(res) == valid:
                nbbon = nbbon+1
                reponse = bonnereponse[random.randint(0, len(bonnereponse)-1)]
            else:
                reponse = '%s, ça fait %i' % (mauvaisereponse[random.randint(0, len(mauvaisereponse)-1)],valid)
            
            reponse = ('%s (%ss)' %(reponse,(datetime.now()-ts).seconds))
            equations.append('%s %s => %s' % (txt,res,reponse))
            nb=nb+1
            print (reponse)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Reviewing multiplication tables for children.',version='0.10')
    parser.add_argument('-f', action='store', dest='firstname',help='firstname of the children',default='firstname')
    results = parser.parse_args()
    
    prenom = results.firstname

    StartMessage(prenom)
    Start(prenom)

