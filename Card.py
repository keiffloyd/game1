import pygame

class Card:
    
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.color = (255, 0, 0)
        self.font = pygame.font.SysFont("Arial", 17)
        self.text = self.font.render("John doe", True, (0,0,0))        
    
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text,(self.x + 22 ,self.y +50))