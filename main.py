import sys
import pygame
from constants import *
from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black = (0, 0, 0, 255)
    FPS = 60

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    asteroidfield = AsteroidField()
    player = Player(x, y)


    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(black)

        for drawable_object in drawable:
            drawable_object.draw(screen)

        for updatable_object in updatable:
            updatable_object.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game Over!")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip() # refresh the screen
        dt = clock.tick(FPS) / 1_000


if __name__ == "__main__":
    main()