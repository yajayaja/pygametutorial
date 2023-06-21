import pygame 
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# Surfaces
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/Ground.png').convert()

score_surf = test_font.render('Runner', False, (64, 64, 64))
score_rect = score_surf.get_rect(midtop = (400, 50))

# Entities
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600, 300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_grav = 0


# Main
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                player_grav = -20

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_grav = -20


    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)

    screen.blit(score_surf, score_rect)

    snail_rect.x -= 4
    if (snail_rect.right) <= 0:
        snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)


    # Player
    player_grav += 1
    player_rect.y += player_grav
    if player_rect.bottom >= 300:
        player_rect.bottom = 300
    screen.blit(player_surf, player_rect)

    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        pygame.mouse.get_pressed()

    pygame.display.update()     # This updates the screen
    clock.tick(60)      # Rate at which it updates