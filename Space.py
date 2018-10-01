# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:10:42 2016

@author: Quentin

La croix est active
"""

#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *
#from random import choice
import time

#Initialisation de la bibliothèque Pygame
pygame.init()



#print("Le programme est lancé")
#                                       ***Variable modifiable***
tempsPause=0.5#0.3 #temps du jeu
nbVitesse=10
deltaVitesse=1
trace = 0
nbColonne=5 #max 33
#                                       ***Fin variable modifiable***
vitesseMax=nbVitesse*deltaVitesse


tailleShip=30
tailleEcran=tailleShip*nbColonne
fenetre = pygame.display.set_mode([tailleEcran, tailleEcran])

ship1 = pygame.image.load("CarreEff.png").convert()
ship2 = pygame.image.load("CarreJ2.png").convert()


carreNoir=pygame.image.load("carreNoir.jpg").convert()


continuer=1
print("\nTouche :")
print("J1 -> zqsd")
print("J2 -> fleches\n")
print("Tapper espace pour jouer\n")
ecran=0

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer=0
    if ecran==0:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer=0
            if event.type==KEYDOWN and (event.key==K_SPACE):
                #print("vous avez tappé sur espace")
                ecran=1
                gameOver=0
                position1=[tailleEcran/2-tailleShip,tailleEcran/2] #position[0] et position[1]
                position2=[tailleEcran/2+tailleShip,tailleEcran/2]
                vecteur1=[0,0]
                vecteur2=[0,0]
                #ecran noir
                i=0
                while i<tailleEcran/30:
                    j=0
                    while j<tailleEcran/30:
                        fenetre.blit(carreNoir,[j*30,i*30])
                        j+=1
                    i+=1
                fenetre.blit(ship1,position1)
                fenetre.blit(ship2,position2)
                pygame.display.flip()
    
    if ecran==1:#si écran play
        time.sleep(tempsPause)
        #check fleche
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer=0
            if event.type==KEYDOWN:#check interuption fleche et zqsd
                #modif vecteur
                #print("une fleche est activé")
                if event.key==K_UP:#K_w
                    #print("h")
                    vecteur2[1]-=deltaVitesse
                elif event.key==K_DOWN:#d
                    vecteur2[1]+=deltaVitesse
                    #print("b")
                if event.key==K_LEFT:#a
                    vecteur2[0]-=deltaVitesse
                    #print("g")
                elif event.key==K_RIGHT:#s
                    vecteur2[0]+=deltaVitesse
                    #print("d") 
                if event.key==K_w:
                    vecteur1[1]-=deltaVitesse
                    #print("z")
                elif event.key==K_s:
                    vecteur1[1]+=deltaVitesse
                    #print("s")
                if event.key==K_a:
                    vecteur1[0]-=deltaVitesse
                    #print("q")
                elif event.key==K_d:
                    vecteur1[0]+=deltaVitesse
                    #print("d")
                    
        #verif vitesseMax sur vecteur1
        if vecteur1[0]<-vitesseMax:
            vecteur1[0]=-vitesseMax
        if vecteur1[0]>vitesseMax:
            vecteur1[0]=vitesseMax
        if vecteur1[1]<-vitesseMax:
            vecteur1[1]=-vitesseMax
        if vecteur1[1]>vitesseMax:
            vecteur1[1]=vitesseMax
        #verif vitesseMax sur vecteur2
        if vecteur2[0]<-vitesseMax:
            vecteur2[0]=-vitesseMax
        if vecteur2[0]>vitesseMax:
            vecteur2[0]=vitesseMax
        if vecteur2[1]<-vitesseMax:
            vecteur2[1]=-vitesseMax
        if vecteur2[1]>vitesseMax:
            vecteur2[1]=vitesseMax
        
        #Calcul de la position suivante 
        position1[0]+=vecteur1[0]
        position1[1]+=vecteur1[1]
        position2[0]+=vecteur2[0]
        position2[1]+=vecteur2[1]

        #verif tailleEcran sur position 1
        if position1[0]<0:
            print("1")
            position1[0]=position1[0]+tailleEcran
        if position1[0]>tailleEcran:
            print("2")
            position1[0]=position1[0]-tailleEcran
        if position1[1]<0:
            print("3")
            position1[1]=position1[1]+tailleEcran
        if position1[1]>tailleEcran:
            print("4")
            position1[1]=position1[1]-tailleEcran
        #verif tailleEcran sur position 2
        if position2[0]<0:
            position2[0]=position2[0]+tailleEcran
        if position2[0]>tailleEcran:
            position2[0]=position2[0]-tailleEcran
        if position2[1]<0:
            position2[1]=position2[1]+tailleEcran
        if position2[1]>tailleEcran:
            position2[1]=position2[1]-tailleEcran

        if trace==0:
            while i<tailleEcran/30:
                j=0
                while j<tailleEcran/30:
                    fenetre.blit(carreNoir,[j*30,i*30])
                    j+=1
                i+=1
        
        #affichage normal
        fenetre.blit(ship1,position1)
        #print(position1)
        #pygame.display.flip()
        fenetre.blit(ship2,position2)
        #pygame.display.flip()

        #test traveré d'un bord pour ship1
        position1V2=position1
        afficheLe1=0
        if position1[0]<0: #à droite
            position1V2[0]=position1[0]+tailleEcran
            afficheLe1=1
        if position1[0]+tailleShip>tailleEcran:
            position1V2[0]=position1[0]-tailleEcran
            afficheLe1=1
        if position1[1]<0:
            position1V2[1]=position1[1]+tailleEcran
            afficheLe1=1
        if position1[1]+tailleShip>tailleEcran:
            position1V2[1]=position1[1]-tailleEcran
            afficheLe1=1
        #test traveré d'un bord pour ship2
        position2V2=position2
        afficheLe2=0
        if position2[0]<0:
            position2V2[0]=position2[0]+tailleEcran
            afficheLe2=1
        if position2[0]+tailleShip>tailleEcran:
            position2V2[0]=position2[0]-tailleEcran
            afficheLe2=1
        if position2[1]<0:
            position2V2[1]=position2[1]+tailleEcran
            afficheLe2=1
        if position2[1]+tailleShip>tailleEcran:
            position2V2[1]=position2[1]-tailleEcran
            afficheLe2=1
        #print("\n ")
        #ecran noir
        i=0
        
        #pygame.display.flip()
        #affichage traversé de bord
        if afficheLe1==1:
            fenetre.blit(ship1,position1V2)
            #pygame.display.flip()
            #print(position1V2)
            #print("afficheLe1=1")
        if afficheLe2==1:
            fenetre.blit(ship2,position2V2)
            #pygame.display.flip()
            #print("afficheLe2=1")
            
        pygame.display.flip()
