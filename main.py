import pygame
from constants import *
from player import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # First create the groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # Then set the containers
    Player.containers = (updatable, drawable)
    
    # Finally create the player (AFTER setting containers)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        # Use the groups instead of the player directly
        updatable.update(dt)
        for drawable_obj in drawable:
            drawable_obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()