import pygame
import sys

pygame.init()

pygame.display.set_caption('Cookie Clicker')
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

cookie_image = pygame.image.load('cookieImage.jpg').convert()
cookie_rect = cookie_image.get_rect(center = (200, 300))
clicked = False
cursor_check = False

cookie_score = 0
cursor_points = 0

main_font = pygame.font.Font(None, 40)
perk_font = pygame.font.Font(None, 32)

def render_text(font, text, pos):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center = pos)
    screen.blit(text_surface,text_rect)
    
while True:
    
    screen.fill((0, 0, 0))
    
    screen.blit(cookie_image, cookie_rect)
    
    mpos = pygame.mouse.get_pos()
    
    if cookie_rect.collidepoint(mpos) and clicked:
        cookie_score += 1
        clicked = False
        
    if cookie_score >= 15 or cursor_check:
        cursor_check = True
        cursor_rect = pygame.Rect(450, 125, 225, 100)
        pygame.draw.rect(screen, (255, 255, 255), cursor_rect, 2)
        render_text(perk_font, f'Cursor: {cursor_points}', cursor_rect.center)
        
    if cookie_score >= 15 and cursor_rect.collidepoint(mpos) and clicked:
        cookie_score -= 15
        clicked = False
        
    
    render_text(main_font, f'Cookies: {cookie_score}', (200, 150))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clicked = False
            
    pygame.display.update()
    clock.tick(60)