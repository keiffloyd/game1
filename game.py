import pygame
import random
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
cards = [card1, card2, card3, card4]

score = 0
time = 10
font = pygame.font.SysFont("Arial", 24)
score_text = font.render("SCORE:", True, (0,0,0))
time_text = font.render("TIME:", True, (0,0,0))
start_time = pygame.time.get_ticks()
update_timer = pygame.time.get_ticks()

def update_card ():
    global start_time
    current = pygame.time.get_ticks()
    if current - start_time > 1000:
        numb = random.randint(0,3)
        for c in cards:
            c.label = False
        cards[numb].label = True
        start_time = current
        
def update_time ():
    global time
    global update_timer
    current = pygame.time.get_ticks()
    if current - update_timer >= 1000:
        time -= 1
        update_timer = current
        
def update_score (pos):
    global score
    for c in cards:
        if c.rect.collidepoint(pos):
            if c.label == True:
                score += 1
                c.label = False

def end_game ():
    global score
    if score == 5:
        screen.fill((144,238,144))
        end_txt = font.render("U WIN!!!", True, (0,0,0))
        screen.blit(end_txt,(250, 250))
        
        

        
while gameloop != False:    
    screen.fill ((255,192,203))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            update_score(event.pos)
            
    score_realtime = font.render(str(score), True,(0,0,0))
    time_realtime = font.render(str(time), True,(0,0,0))
    
    screen.blit(score_text, (20,30))
    screen.blit(time_text, (20,60))
    screen.blit(score_realtime, (100,30))
    screen.blit(time_realtime, (100,60))
    #if
    
    
    # card1.draw(screen)
    # card2.draw(screen)
    # card3.draw(screen)
    # card4.draw(screen)
    for c in cards:
        c.draw(screen)
        
    update_card()
    update_time()
    end_game()
    
    pygame.display.update()
    
pygame.quit()