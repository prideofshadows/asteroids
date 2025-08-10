# this allows us to use code from the open-source pygame library throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()  # Initialize all imported pygame modules
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()  # Create a clock object to manage frame rate
    dt=0  # Initialize delta time variable

    updateable = pygame.sprite.Group()  # Create a group for updateable sprites
    drawable = pygame.sprite.Group()  # Create a group for drawable sprites
    asteroids = pygame.sprite.Group()  # Create a group for asteroids
    shots = pygame.sprite.Group()  # Create a group for shots
    
    Asteroid.containers = (updateable, drawable, asteroids)  # Add asteroids to all groups
    Player.containers = (updateable, drawable)  # Add player to both groups
    AsteroidField.containers = updateable # Add asteroid field to updateable group
    Shot.containers = (shots, updateable, drawable)  # Add shots to the shots group

    # Create a player instance at the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # Create an asteroid field instance
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updateable.update(dt)   

        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.detect_collision(shot):
                    shot.kill()
                    asteroid.split()
         
        screen.fill("black")

        for draw in drawable: 
            draw.draw(screen)  # Draw all drawable sprites
            
        pygame.display.flip()  # Update the full display Surface to the screen
        dt = clock.tick(60 )/ 1000 # Limit the frame rate to 60 FPS

if __name__ == "__main__":
    main()
