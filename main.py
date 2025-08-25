import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    score = 0
    lives = 3

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        #player.update(dt)
        #player.draw(screen)

        #Update
        if pygame.key.get_pressed()[pygame.K_q]:
            running = False
            print(f"Final Score: {score}")
            sys.exit(0)
        updatable.update(dt)

        for a in asteroids:
            for s in shots:
                if a.checkCollision(s):
                    score += 1
                    a.split()
                    s.kill()

        for a in asteroids:
            if not isinstance(a, Player):
                if a.checkCollision(player):
                    if lives == 0:
                        print("Game Over!")
                        print(f"Final Score: {score}")
                        sys.exit(1)
                    lives -= 1

        #Draw
        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()
        timePassed = clock.tick(60)
        dt = timePassed / 1000

if __name__ == "__main__":
    main()
