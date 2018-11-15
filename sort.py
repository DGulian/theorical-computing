from random import *

def triInsertion(liste):
    compteur=0
    for i in range(1,len(liste)):
        nb=liste[j]
        i=j-1
        compteur+=1
        while((liste[i]>nb) and i>=0)):
            liste[i+1]=liste[i]
            i=i-1
            compteur+=1
        liste[i+1]=nb
    return liste


def triSelection(liste):
    compteur=O
    for fin in range(len(liste)-1,0,-1):
        max=0
        for j in range(1,fin+1):
            compteur+=1
            if liste[j]>liste[max]:
                max=j
        liste[max],liste[fin]=liste[fin],liste[max]
    return liste


def triBulle(liste):
    compteur=0
    interversion=True
    while interversion:
        interversion=False
        for i in range(len(liste)-1):
            compteur+=1
            if liste[i]<liste[i+1]:
                liste[i],liste[i+1]=liste[i+1],liste[i]
                interversion=True
    return liste


def triBulleOpt(liste):
    compteur=0
    intereversion=True
    etape=1
    while interversion:
        interversion=False
        for i in range(len(liste)-etape):
            compteur+=1
            if liste[i]>liste[i+1]:
                liste[i],liste[i+1]=liste[i+1],liste[i]
                interversion=True
            etape+=1
        return liste
    
    
def triRapide(liste):
    compteur=0
    if len(liste)<=1:
        return liste
    else
        pivor=liste[0]
        inf=[]
        sup=[]
        for nombre in liste[1:]:
            compteur+=1
            if nombre<pivot:
                inf.append(nombre)
            else:
                sup.append(nombre)
        inf=triRapide(inf)
        sup=triRapide(sup)
        return inf+[pivot]+sup
    
    
def triFusion(liste):
    compteur=0
    if len(liste)<=1:
        return liste
    else:
        n=len(liste)
        m1=triFusion(l[:n//2])
        m2=triFusion(l[n//2:])
        fusion=[]
        i,j=0,0
        while i<len(m1) and j < len(m2):
            compteur+=1
                if m1[i]<m2[j]
                    fusion.append(m1[i])
                    i=i+1
                else:
                    fusion.append(m2[j])
                    j=j+1
        fusion=fusion+m1[i:]+m2[j:]
        return fusion
        
