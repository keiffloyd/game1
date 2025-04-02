import pygame
from Card import Card

pygame.init()
screen = pygame.display.set_mode((600, 600))
card_w = 100
card_h = 120
gameloop = True
card1 = Card(30,230,card_w,card_h)
card2 = Card(170,230,card_w,card_h)
card3 = Card(320,230,card_w,card_h)
card4 = Card(470,230,card_w,card_h)
score = 0
time = 10
font = pygame.font.SysFont("Arial", 24)
score_text = font.render("SCORE:", True, (0,0,0))
time_text = font.render("TIME:", True, (0,0,0))


while gameloop != False:
    screen.fill ((255,192,203))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    score_realtime = font.render(str(score), True,(0,0,0))
    time_realtime = font.render(str(time), True,(0,0,0))
    
    #if
    score = score + 1
    time = time - 1 
    
    
    card1.draw(screen)
    card2.draw(screen)
    card3.draw(screen)
    card4.draw(screen)
    screen.blit(score_text, (20,30))
    screen.blit(time_text, (20,60))
    screen.blit(score_realtime, (100,30))
    screen.blit(time_realtime, (100,60))
    pygame.display.update()
    
pygame.quit()