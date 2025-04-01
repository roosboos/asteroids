import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # First create the groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Then set the containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots,updatable,drawable)
    
    # Finally create the player (AFTER setting containers)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # create an AsteroidField instance
    asteroid_field = AsteroidField()

    # Game Loop starts here
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        # update all objects
        updatable.update(dt)
        
        #add collision code
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                import sys
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()
                    break
        
        #draw all objects
        for drawable_obj in drawable:
            drawable_obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()