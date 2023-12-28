import pygame

pygame.init() #Se inicializa pygame
screen = pygame.display.set_mode([500, 500]) #Se crea una ventana

running = True

while running:
    for event in pygame.event.get():# Se verifica si el usuario cerro la ventana
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))# Se pinta el fondo de la ventana
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    pygame.display.flip()# Muestra los cambios en la pantalla
pygame.quit() # Fin