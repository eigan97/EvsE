import socket
import threading
import sys
import pickle
import pygame
from pygame.locals import *
from random import randint
Pposx=0
Pposx2=580
golpe=False
golpe2=False
nueva=0
nueva2=0
patada=False
patada2=False
nuevap=0
nuevap2=0
cont=6
cont2=6
direc=True
direc2=True
i=0
i2=0
xixf={}#xinicial y xfinal
Rxixf={}#reversa
rectangulo=0
rectangulo2=0
vida1=100
vida2=100

# class Cliente():
# 	"""docstring for Cliente"""
# 	def __init__(self, host="localhost", port=4000):
		
# 		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 		self.sock.connect((str(host), int(port)))

# 		msg_recv = threading.Thread(target=self.msg_recv)

# 		msg_recv.daemon = True
# 		msg_recv.start()
# 	def msg_recv(self):
# 		while True:
# 			try:
# 				data = self.sock.recv(1024)
# 				if data:
# 					print(pickle.loads(data))
# 			except:
# 				pass

# 	def send_msg(self, msg):
# 		self.sock.send(pickle.dumps(msg))


def imagen(imagenfile, transparent=False)  :
	try: imagen=pygame.image.load(imagenfile)
	except pygame.error:
			raise SystemExit
	imagen.convert()
	if transparent:
		color=imagen.get_at((0,0))
		imagen.set_colorkey(color, RLEACCEL)
	return imagen
def teclado():
	teclado=pygame.key.get_pressed()
	global Pposx,golpe,patada,Pposx2,golpe2,patada2,rectangulo2,rectangulo
	global cont, direc,cont2, direc2
	if teclado[K_d] and Pposx2<=745:
		Pposx2+=5
		cont2+=1
		direc2=False
	elif teclado[K_a] and Pposx2>0:
		if rectangulo.colliderect(rectangulo2) or rectangulo2.colliderect(rectangulo):
			Pposx2+=0
			cont2+=1
			direc2=True
		else:
			Pposx2-=5
			cont2+=1
			direc2=True
	elif teclado[K_u]:
		golpe2=True
	elif teclado[K_i]:
		patada2=True
	elif teclado[K_w]:
		Pposx-=2


#jugador 1 
	if teclado[K_RIGHT] and Pposx<=745:
		if rectangulo.colliderect(rectangulo2) or rectangulo2.colliderect(rectangulo):
			Pposx+=0
			cont+=1
			direc=True
		else:
			Pposx+=5
			cont+=1
			direc=True
	elif teclado[K_LEFT] and Pposx>0:
		Pposx-=5
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
def sprite():
 
    global cont, cont2
  # xixf[0]=(0,0,20,41)
  #   xixf[1]=(22,0,25,41)
  #   xixf[2]=(47,0,25,41)
  #   xixf[3]=(73,0,20,41)
  #   xixf[4]=(93,0,27,41)
  #   xixf[5]=(120,0,27,41)
    xixf[0]=(0,0,150,300)
    xixf[1]=(200,0,180,300)
    xixf[2]=(390,0,180,300)
    xixf[3]=(590,0,180,300)
    xixf[4]=(0,0,0,0)
    
   
   
    Rxixf[0]=(590,0,290,300)
    Rxixf[1]=(390,0,200,300)
    Rxixf[2]=(200,0,200,300)
    Rxixf[3]=(0,0,170,300)
    Rxixf[4]=(0,0,0,0)
    p=6
    p2=6
   	
	
    global i, i2
       
    if cont==p:
        i=0
   
    if cont==p*2:
        i=1
   
    if cont==p*3:
        i=2
   
    if cont==p*4:
                i=3
                cont=0

       	#2
    if cont2==p2:
        i2=0
   
    if cont2==p2*2:
        i2=1
   
    if cont2==p2*3:
        i2=2
   
    if cont2==p2*4:
                i2=3
                cont2=0
   
    return

def juego():
	pygame.init()
	ventana=pygame.display.set_mode((900,600))
	pygame.display.set_caption("EVSE")
	

	edgar=imagen('imagenes/caminar.png',True)
	edgarPelear=imagen('imagenes/golpe.png',True)
	edgarPelearA=pygame.transform.flip(edgarPelear,True,False)
	edgarPatada=imagen('imagenes/patada.png',True)
	edgarPatadaA=pygame.transform.flip(edgarPatada,True,False)
	edgar_atras=pygame.transform.flip(edgar,True,False)

	edgar2=imagen('imagenes/caminarB.png',True)
	edgarPelear2=imagen('imagenes/golpeB.png',True)
	edgarPelearA2=pygame.transform.flip(edgarPelear2,True,False)
	edgarPatada2=imagen('imagenes/patadaB.png',True)
	edgarPatadaA2=pygame.transform.flip(edgarPatada2,True,False)
	edgar_atras2=pygame.transform.flip(edgar2,True,False)
	# vida=100
	# posX=0
	# posY=0
	# rectangulo2=pygame.Rect(200,200,100,50)
	# velocidad=2

	blanco=(255,255,255)

	clock=pygame.time.Clock()
	# derecha=True
				# no se va c = Cliente()
	# rectangulo=pygame.Rect(0,0,100,50)
	while True:
		
		time=clock.tick(100)
		sprite()
		teclado()

		global golpe, patada, golpe2, patada2,rectangulo2, rectangulo
		pygame.display.init()
		ventana.fill(blanco)
		
		rectangulo=pygame.Rect(Pposx,318,120,230)
		rectangulo2=pygame.Rect(Pposx2,318,120,230)
		pygame.draw.rect(ventana,(255,255,255),rectangulo2)
		pygame.draw.rect(ventana,(255,255,255),rectangulo)
		

		

		if direc2==True and golpe2==False and patada2==False:
			ventana.blit(edgar_atras2, (Pposx2,318),(Rxixf[i2]))

		if direc==True and golpe==False and patada==False:
			ventana.blit(edgar, (Pposx,318),(xixf[i]))	

		if direc2==False and golpe2==False and patada2==False:
			ventana.blit(edgar2, (Pposx2,318),(xixf[i2]))

		if direc==False and golpe==False and patada==False:
			ventana.blit(edgar_atras, (Pposx, 318),(Rxixf[i]))

#
#
#22222222222222222222222
#			
#
#
#
#
		if golpe2==True and direc2==True:
			global nueva2,vida2,vida1
			ventana.blit(edgarPelearA2, (Pposx2, 318),(Rxixf[nueva2]))
			ventana.blit(edgar_atras2, (Pposx2,318),(Rxixf[4]))
			tiempo=pygame.time.Clock()
			tiempo2=tiempo.tick(50)
			nueva2+=1
			if nueva2==4:
				golpe2=False
				nueva2=0
			if rectangulo.colliderect(rectangulo2) or rectangulo2.colliderect(rectangulo):
				vida1-=.5
				
		if golpe2==True and direc2==False:
			ventana.blit(edgarPelear2, (Pposx2, 318),(xixf[nueva2]))
			ventana.blit(edgar2, (Pposx2,318),(xixf[4]))
			tiempo=pygame.time.Clock()
			tiempo2=tiempo.tick(50)
			nueva2+=1
			if nueva2==4:
				golpe2=False
				nueva2=0
			if rectangulo.colliderect(rectangulo2) or rectangulo2.colliderect(rectangulo):
				vida1-=.5
#
#
#
#
#
		if golpe==True and direc==True:
			global nueva
			ventana.blit(edgarPelear, (Pposx, 318),(xixf[nueva]))
			ventana.blit(edgar, (Pposx,318),(xixf[4]))
			tiempo=pygame.time.Clock()
			tiempo2=tiempo.tick(50)
			nueva+=1
			if nueva==4:
				golpe=False
				nueva=0
			if rectangulo.colliderect(rectangulo2) or rectangulo2.colliderect(rectangulo):
				vida2-=.5
		if golpe==True and direc==False:
			ventana.blit(edgarPelearA, (Pposx, 318),(Rxixf[nueva]))
			ventana.blit(edgar_atras, (Pposx,318),(Rxixf[4]))
			
			tiempo=pygame.time.Clock()
			tiempo2=tiempo.tick(50)
			nueva+=1
			if nueva==4:
				golpe=False
				nueva=0
			if rectangulo.colliderect(rectangulo2) or rectangulo2.colliderect(rectangulo):
				vida2-=.5

#
#
#
#222222222222222222222222
#
#
		if patada2==True and direc2==True and golpe2==False:
			global nuevap2
			ventana.blit(edgarPatadaA2, (Pposx2, 318),(Rxixf[nuevap2]))
			ventana.blit(edgar_atras2, (Pposx2,318),(Rxixf[4]))
			
			tiempo3=pygame.time.Clock()
			tiempo4=tiempo3.tick(50)
			nuevap2+=1

			if nuevap2==4:
				patada2=False
				nuevap2=0
			if rectangulo.colliderect(rectangulo2) or rectangulo2.colliderect(rectangulo):
				vida1-=1
		if patada2==True and direc2==False and golpe2==False:
			ventana.blit(edgarPatada2, (Pposx2, 318),(xixf[nuevap2]))
			ventana.blit(edgar2, (Pposx2,318),(xixf[4]))
			tiempo3=pygame.time.Clock()
			tiempo4=tiempo3.tick(50)
			nuevap2+=1
			if nuevap2==4:
				patada2=False
				nuevap2=0
			if rectangulo.colliderect(rectangulo2) or rectangulo2.colliderect(rectangulo):
				vida1-=1



#
#
#
#
#
#

		if patada==True and direc==True and golpe==False:
			global nuevap
			ventana.blit(edgarPatada, (Pposx, 318),(xixf[nuevap]))
			ventana.blit(edgar, (Pposx,318),(xixf[4]))
			tiempo3=pygame.time.Clock()
			tiempo4=tiempo3.tick(50)
			nuevap+=1

			if nuevap==4:
				patada=False
				nuevap=0
			if rectangulo.colliderect(rectangulo2) or rectangulo2.colliderect(rectangulo):
				vida2-=1
		if patada==True and direc==False and golpe==False:
			ventana.blit(edgarPatadaA, (Pposx, 318),(Rxixf[nuevap]))
			ventana.blit(edgar_atras, (Pposx,318),(Rxixf[4]))
			tiempo3=pygame.time.Clock()
			tiempo4=tiempo3.tick(50)
			nuevap+=1
			if nuevap==4:
				patada=False
				nuevap=0
			if rectangulo.colliderect(rectangulo2) or rectangulo2.colliderect(rectangulo):
				vida2-=1



		pygame.display.flip()	
		# pygame.draw.rect(ventana,(180,70,70),rectangulo2)
		# pygame.draw.rect(ventana,(180,70,70),rectangulo)
		# rectangulo.left,rectangulo.top=pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == QUIT or vida2<=0 or vida1<=0:
				pygame.quit()
				sys.exit()
				# no se va self.sock.close()

			elif event.type==pygame.KEYDOWN:
				if event.key==K_LEFT:
					# vida=vida-1
					# c.send_msg(vida)
					pass
		print(vida2)
		print(vida1)
		pygame.display.update()
j=juego()






	
