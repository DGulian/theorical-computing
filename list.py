from math import *
from random import *

list0=[1,2,3,4,5,6,7,8,9]
list1=[9,10,11,12,13,14,15,16,17,18,19]

# Function who merge 2 lists and remove his duplicates
def fusion(list0, list1):
    
    list2 = []
    list2.extend(list0)
    list2.extend(list1)
    for i in list0:
        if i in list1:
            list2.remove(i)
            print("No more duplicate")
            print(list2)
        
#fusion(list0,list1)


#Function who give sum and average of a list
def average(list0):
    add=sum(list0)
    average = sum(list0)/len(list0)

    print("Sum = ", add, "Average = " ,average)

#average(list0)


#Function who return the index of an element in a list, return -1 if no elements
def position(list0):
    n = int(input("choose")) 
    if n in list0:
         print(list0[n-1])
    else:
        return -1

#position(list0)

def supPair(list0):
    for i in list0:
        if i%2 == 0:
            list0.remove(i)
        print(list0)
#supPair(list0)

"""
Exercice 2
"""

def commun(list0, list1):
    commun=[]
    for i in list0:
        if i in list1:
            commun.append(i)
        print(commun)
#commun("Julien","Gulian")


"""
Exercice 3
"""

def dice():
    nb = 10
    acc = 0
    while(nb!=0):
        dice = randint(1,6)
        if dice == 5 or dice == 6:
            acc = acc + 1
            print(acc)
        elif dice == 6:
            acc = acc + 1
        nb = nb -1
#dice()


def distance(p1,p2):
    return(sqrt((p2[0] - p1[0])**2 + (p2[1]-p1[1])**2))

def orderPoints(points):
    distances = []
    for p in points:
        distances.append(distance((0,0),p))
    print(sorted(distances))

#point=[(1,2),(5,4),(6,2),(8,0),(4,6)]
#orderPoints(point)
def dardsLaunching(n):
    for i in range (n):
        x = randint(-10,10)
        y = randint(-10,10)
        score = (distance((0,0),(x,y)))
        point = 11 - ceil(score)
    return point

def dardsGame():
    nbDards = 4
    nbPlayer = 2 #int(input("Choose a number of player (max:5)"))
    for i in range(1,nbPlayer+1):
        dardsLaunching(nbDards)
        print(point)

dardsGame()
    


        
    
        
