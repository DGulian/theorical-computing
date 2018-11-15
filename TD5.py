import math
def stop():
    x = 0
    liste=[]
    while x >= 0:
        x = int(input("blabla"))
        if x>0:
            liste.append(x)
        else:
            break
    print(liste)



def comp(a,b):
    if a<b:
        return True
    else:
        return False


def triFusion(liste):
    compteur=0
    if len(liste)<=1:
        return liste
    else:
        n=len(liste)
        m1=triFusion(liste[:n//2])
        m2=triFusion(liste[n//2:])
        fusion=[]
        i,j=0,0
        while i<len(m1) and j < len(m2):
            compteur+=1
            if m1[i]<m2[j]:
                fusion.append(m1[i])
                i=i+1
            else:
                    fusion.append(m2[j])
                    j=j+1
        fusion=fusion+m1[i:]+m2[j:]
        return fusion
    
def triBulle(liste):
    compteur=0
    interversion=True
    while interversion:
        interversion=False
        for i in range(len(liste)-1):
            compteur+=1
            if liste[i]>liste[i+1]:
                liste[i],liste[i+1]=liste[i+1],liste[i]
                interversion=True
    return liste


liste =[567,4578,735,6423,124321,2134,1253,213,4321,234,56,3457,8746,234,12,23,34,45,56,67]


def op(liste,a):
    liste=triBulle(liste)
    print(liste)
    
    for i in range(len(liste)):
        if liste[i]<a:
            print (liste[i])        
    print(sum(liste))
    print(sum(liste)/float(len(liste)))
    
    for j in range(len(liste)):
        print(math.floor(liste[j]))
        
    for w in range(len(liste)):
        if liste[w]%2==0:
            print(liste[w])

op(liste, 900)                 


def triSelection(liste):
    for fin in range(len(liste)-1,0,-1):
        max=0
        for j in range(1,fin+1):
            if liste[j]>liste[max]:
                max=j
        liste[max],liste[fin]=liste[fin],liste[max]
    return liste

print(triSelection(liste))


def equation_droite(xa, ya, xb, yb): 
    a = (yb-ya)/(xb-xa) 
    b = ya-a*xa 

    


