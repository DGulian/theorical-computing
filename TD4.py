from random import *
from math import *

def multiplication_grille(x):
    b = ""
    if x==0:
        return 
    else:
        for i in range(1,11):
            a = i * x
            b = b + str(a) + " | " 
            print(b)
        return multiplication(x-1)


def justePrix():
    x = randint(0,1000)
    guess = int(input("Entrez votre juste prix"))

    while guess != x :
        if guess > x:
           guess = int(input("C'est moins !"))
        else:
            guess = int(input("C'est plus"))
    if guess == x:
        print("Félication vous etes un gros k-sos")

def multiplication(x,y):
    rslt = 0
    for i in range(y):
        rslt = rslt +x
    return rslt

def premier(n):
    prems = [3] # liste des nombres premiers initialisée à 3
    i = 5
    while len(prems) < n:
            
            pmax = int(sqrt(i)) # inutile de tester au delà de sqrt(i)
            for prem in prems:
                    if prem>pmax: # i est premier: on le garde et on passe au i suivant
                            prems.append(i)
                            break
                    if i%prem==0: # i n'est pas 1er: on passe au i suivant
                            break
            i = i+2
    print(prems)

premier(100)


def guessFirst(n):
    element = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    passwd = ""
 
    for i in range(n):
        passwd = passwd + element[randint(0, len(element) - 1)]
    print(passwd)

    element = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    dico=""
    while dico!=passwd:
        for j in range(n):
            dico = dico + element[randint(0, len(element) - 1)]
            print(dico)
            if len(dico)==len(passwd) and dico!=passwd:
                dico=""
    print (passwd,dico)
        
guessFirst(3)


