import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()
ventana=pygame.display.set_mode((600,300))
pygame.display.set_caption("EVSE")
vida=100
posX=0
posY=0
rectangulo2=pygame.Rect(200,200,100,50)
velocidad=2
blanco=(255,255,255)
derecha=True

rectangulo=pygame.Rect(0,0,100,50)
while True:
	pygame.display.init()
	ventana.fill(blanco)
	pygame.draw.rect(ventana,(180,70,70),rectangulo2)
	pygame.draw.rect(ventana,(180,70,70),rectangulo)
	rectangulo.left,rectangulo.top=pygame.mouse.get_pos()
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		elif event.type==pygame.KEYDOWN:
			if rectangulo.colliderect(rectangulo2) and event.key==K_LEFT:
				vida=vida-1
				print(vida)

	
	if derecha==True:
		if posX<400:
			posX+=velocidad
			rectangulo2.left=posX
		else:
			derecha=False
	else:
		if posX>1:
			posX-=velocidad
			rectangulo2.left=posX
		else:
			derecha=True
	pygame.display.update()


