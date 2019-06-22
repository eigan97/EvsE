import socket
import threading
import sys
import pickle
import pygame
from pygame.locals import *
from random import randint
Pposx=0;
Pposy =318

cont=6
direc=True
i=0
xixf={}#xinicial y xfinal
Rxixf={}#reversa

parabola={}
salto = False
 
salto_Par=False

class Cliente():
	"""docstring for Cliente"""
	def __init__(self, host="localhost", port=4000):
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((str(host), int(port)))

		msg_recv = threading.Thread(target=self.msg_recv)

		msg_recv.daemon = True
		msg_recv.start()
	def msg_recv(self):
		while True:
			try:
				data = self.sock.recv(1024)
				if data:
					print(pickle.loads(data))
			except:
				pass

	def send_msg(self, msg):
		self.sock.send(pickle.dumps(msg))

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
	global Pposx
	global cont, direc, salto, salto_Par
	
    

	# if teclado[K_RIGHT]:
	# 	Pposx+=2
	# 	cont+=1
	# 	direc=True
	# elif teclado[K_LEFT]:
	# 	Pposx-=2
	# 	cont+=1
	# 	direc=False

	##########1#######################################
	if teclado[K_q] and teclado[K_RIGHT] and salto_Par==False:
		salto_Par=True
	elif teclado[K_q] and teclado[K_LEFT] and salto_Par==False:
		salto_Par=True
         
	elif teclado[K_RIGHT]and salto==False and salto_Par==False:
		Pposx+=2
		cont+=1
		direc=True
	elif teclado[K_LEFT]and salto==False and salto_Par==False:
		Pposx-=2
		cont+=1
		direc=False
	elif teclado[K_q] and salto==False and salto_Par==False:
		salto=True          
	else :
		cont=4

def sprite():
 
    global cont
  # xixf[0]=(0,0,20,41)
  #   xixf[1]=(22,0,25,41)
  #   xixf[2]=(47,0,25,41)
  #   xixf[3]=(73,0,20,41)
  #   xixf[4]=(93,0,27,41)
  #   xixf[5]=(120,0,27,41)
    xixf[0]=(0,0,120,200)
    xixf[1]=(122,0,120,200)
    xixf[2]=(245,0,120,210)
    xixf[3]=(370,0,135,200)
    
   
   
    Rxixf[0]=(380,0,120,200)
    Rxixf[1]=(255,0,120,200)
    Rxixf[2]=(125,0,120,200)
    Rxixf[3]=(0,0,120,200)
   
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

def juego():
	pygame.init()
	ventana=pygame.display.set_mode((1360,700))
	pygame.display.set_caption("EVSE")
	edgar=imagen('imagenes/edgar.png',True)
	edgar_atras=pygame.transform.flip(edgar,True,False)
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
	global salto_Par  
	bajada=False
	bajada_Par=False
	while True:
		
		time=clock.tick(60)
		sprite()
		teclado()

		
		pygame.display.init()
		ventana.fill(blanco)
		global Pposx,Pposy,salto
		if direc==True and salto==False:
			ventana.blit(edgar, ( Pposx, Pposy),(xixf[i]))
		if direc==False and salto==False:
			ventana.blit(edgar_atras, ( Pposx, Pposy),(Rxixf[i]))
       #salto normal
		if salto==True:            
			if direc==True:
				ventana.blit(edgar, ( Pposx, Pposy),(xixf[3]))
			if direc==False:
				ventana.blit(edgar_atras, ( Pposx, Pposy),(Rxixf[3]))  
           
			if bajada==False:
				Pposy-=4              
               
			if bajada==True:
				Pposy+=4              
           
			if Pposy==186:
				bajada=True
           
			if Pposy==318:
				bajada=False
				salto=False
        #==============================  
       
        #SALTO PARABOLICO
		if salto_Par==True and direc==True:            
           
			ventana.blit(edgar, ( Pposx, Pposy),(xixf[3]))
           
			if bajada_Par==False:
				Pposy-=3
				Pposx+=2
               
			if bajada_Par==True:
				Pposy+=3
				Pposx+=2

			if Pposy==246:
				bajada_Par=True
           
			if Pposy==318:
				bajada_Par=False
				salto_Par=False
		elif salto_Par==True and direc==False:            
           
			ventana.blit(edgar_atras, ( Pposx, Pposy),(Rxixf[3]))
           
			if bajada_Par==False:
				Pposy-=3
				Pposx-=2
               
			if bajada_Par==True:
				Pposy+=3
				Pposx-=2
           
			if Pposy==246:
				bajada_Par=True
           
			if Pposy==318:
				bajada_Par=False
				salto_Par=False  
		# if direc==True:
		# 	ventana.blit(edgar, (Pposx,318),(xixf[i]))
			
		# if direc==False:
		# 	ventana.blit(edgar_atras, (Pposx, 318),(Rxixf[i]))
		pygame.display.flip()	
		# pygame.draw.rect(ventana,(180,70,70),rectangulo2)
		# pygame.draw.rect(ventana,(180,70,70),rectangulo)
		# rectangulo.left,rectangulo.top=pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
				# no se va self.sock.close()

			elif event.type==pygame.KEYDOWN:
				if event.key==K_LEFT:
					# vida=vida-1
					# c.send_msg(vida)
					pass
		
		pygame.display.update()
j=juego()






	