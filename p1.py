import pygame

pygame.init()
screen = pygame.display.set_mode((400, 600))
player = pygame.Rect(0 , 0, 50, 50)
speed = 50
clock = pygame.time.Clock()

running = True
while running:
    delta_time = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((200,100,230))
    pygame.draw.rect(screen, (0 ,0, 0), player)
    player.x += speed * delta_time
    if player.x >= 350:
        player.x = 350
        speed = -50
    if player.x <= 0:
        speed = 50
    pygame.display.update()
            
pygame.quit()