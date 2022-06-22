import pygame, sys

pygame.init()

wIDTH = 1400
hEIGHT = 760
# rgb: red green blue
rED = (247, 243 , 222)

screen = pygame.display.set_mode( (wIDTH, hEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE')
screen.fill( rED )

Plantimg1 = pygame.image.load('./images/2.png')
Plantimg2 = pygame.image.load('./images/6.png')
Plantimg2 = pygame.transform.smoothscale(Plantimg2, (700, 600)) 
Plantimg2 = pygame.transform.rotate(Plantimg2, -23)
Plantimg3 = pygame.image.load('./images/4.png')
Plantimg3 = pygame.transform.smoothscale(Plantimg3, (650, 550))
Plantimg3 = pygame.transform.rotate(Plantimg3, (-70 ))
Plantimg4 = pygame.image.load('./images/5.png')
Plantimg4 = pygame.transform.smoothscale(Plantimg4, (650, 550))
Plantimg4 = pygame.transform.flip(Plantimg4, True, False)
Plantimg5 = pygame.image.load('./images/1.png')
Plantimg5 = pygame.transform.smoothscale(Plantimg5, (550, 450))
Plantimg6 = pygame.image.load('./images/3.png')
Plantimg6 = pygame.transform.smoothscale(Plantimg6, (550,450))
Plantimg6 = pygame.transform.rotate(Plantimg6, (-30))
Plantimg7 = pygame.image.load('./images/Naamloos.png')
Plantimg7 = pygame.transform.smoothscale(Plantimg7, (550, 450))
Plantimg7 = pygame.transform.rotate(Plantimg7, (-90))
# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()       

    screen.blit(Plantimg1, (-200, -200)) 
    screen.blit(Plantimg3, (-200, 200))
    screen.blit(Plantimg2, (-290, -20 ))
    screen.blit(Plantimg5, (1120, 100))
    screen.blit(Plantimg4, (1070, -100))
    screen.blit(Plantimg7, (1200, 380))
    screen.blit(Plantimg6, (1100, 110))
    
   