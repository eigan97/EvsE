#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame
from pygame.locals import *
from time import clock
from pygame.constants import K_q
 
 
#Tamaño  la pantalla
WIDTH = 900
HEIGHT = 500
 
# Variables
Pposx=0
golpe=False
nueva=0
patada=False
nuevap=0
cont=6
direc=True
i=0
xixf={}#xinicial y xfinal
Rxixf={}#reversa
 
 
def Initialize():
   
    global screen, clock,xixf,Rxixf
   
    pygame.init()    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mario")
    clock = pygame.time.Clock()
   
    xixf={}
    Rxixf={}
   
    xixf[0]=(0,0,120,200)
    xixf[1]=(122,0,120,200)
    xixf[2]=(245,0,120,210)
    xixf[3]=(370,0,135,200)
    xixf[4]=(0,0,0,0)
    
   
   
    Rxixf[0]=(380,0,120,200)
    Rxixf[1]=(255,0,120,200)
    Rxixf[2]=(125,0,120,200)
    Rxixf[3]=(0,0,120,200)
    Rxixf[4]=(0,0,0,0)
   
    return
 
def LoadContent():
   
   	global fondo, mario,mario_inv  
	
	edgar= imagen('imagenes/edgar.png', True)
	edgarPelear=imagen('imagenes/edgarHitSheet.png',True)
	edgarPelearA=pygame.transform.flip(edgarPelear,True,False)
	edgarPatada=imagen('imagenes/ko (1).png',True)
	edgarPatadaA=pygame.transform.flip(edgarPatada,True,False)
	edgar_atras=pygame.transform.flip(edgar,True,False)
   
   
    return
 
def Updates():
   
    teclado()    
    #Escenario
    sprite_M()  
    #Enemigo()
    #Coliciones()
   
    return
 
 
 
def Draw():
   
    global salto,salto_Par, salto,bajada_Par,bajada
   
   
   
    screen.blit(fondo, (0, 0))
       
       
    global MposX,MposY
       
    if direc==True and salto==False :
        screen.blit(mario, ( MposX, MposY),(xixf[i]))
   
    if direc==False and salto==False :
        screen.blit(mario_inv, ( MposX, MposY),(Rxixf[i]))
       
       
       #salto normal y Parabolico
    if salto==True:            
           
        if direc==True:
            screen.blit(mario, ( MposX, MposY),(xixf[4]))
        if direc==False:
            screen.blit(mario_inv, ( MposX, MposY),(Rxixf[4]))  
           
        if bajada==False:
            MposY-=4              
               
        if bajada==True:
            MposY+=4              
           
        if MposY<=186:
            bajada=True
           
        if MposY>=318:
            bajada=False
            salto=False
        #==============================  
       
       
   
           
   
    pygame.display.flip()
   
    return
 
 
 
 
 
#===========================================================
#=================IMAGEN====================================
 
def imagen(filename, transparent=False):
       try: imagen=pygame.image.load(imagenfile)
	except pygame.error:
			raise SystemExit
	imagen.convert()
	if transparent:
		color=imagen.get_at((0,0))
		imagen.set_colorkey(color, RLEACCEL)
	return imagen
#================================================================
 
 
#======================TECLADO===================================
#================================================================
 
 
def teclado():
   
   global Pposx,golpe,patada
	global cont, direc 
	if teclado[K_RIGHT]:
		Pposx+=2
		cont+=1
		direc=True
	elif teclado[K_LEFT]:
		Pposx-=2
		cont+=1
		direc=False
	elif teclado[K_x]:
		golpe=True
	elif teclado[K_z]:
		patada=True
	elif teclado[K_UP]:
		Pposx-=2

	else:
		pass
    # Cerrar la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
   
         
    return
 
 
 
#===================SPRITE===============================
#========================================================
def sprite_M():
 
    global cont

     
    p=6
   
    global i
       
    if cont==p:
        i=0
   
    if cont==p*2:
        i=1
   
    if cont==p*3:
        i=2
   
    if cont==p*4:
        i=3
       	cont=0
    return
def main():
    Initialize()
    LoadContent()
    while True:
        time = clock.tick(60)
        Updates()
        Draw()     
        #if gameOver==True
            #UnLoadContent()
    return 
if __name__ == '__main__':
    main()