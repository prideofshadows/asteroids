# this allows us to use code from the open-source pygame library throughout this file
import pygame
from constants import *
from player import Player

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
    
    Player.containers = (updateable, drawable)  # Add player to both groups

    # Create a player instance at the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        for draw in drawable:
            draw.draw(screen)  # Draw all drawable sprites
        pygame.display.flip()  # Update the full display Surface to the screen
        dt = clock.tick(60 )/ 1000 # Limit the frame rate to 60 FPS
        updateable.update(dt)


if __name__ == "__main__":
    main()
