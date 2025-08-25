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

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player_start_pos_x = SCREEN_WIDTH / 2
    player_start_pos_y = SCREEN_HEIGHT /2
    player = Player(player_start_pos_x, player_start_pos_y)
    asteroidField = AsteroidField()
    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f"Final Score: {score}")
                return
        screen.fill((0, 0, 0))

        #Update
        updatable.update(dt)

        for a in asteroids:
            for s in shots:
                if a.checkCollision(s):
                    score += a.split()
                    s.kill()

        playerDied = False
        for a in asteroids:
            if a.checkCollision(player):
                playerDied = True
                player.lives -= 1
                if player.lives == 0:
                    print("Game Over!")
                    print(f"Final Score: {score}")
                    sys.exit(1)
                print(f"Lives Remaining: {player.lives}")
                player.hasCollision = False
        
        if playerDied:
            for a in asteroids:
                a.kill()
            player.respawn(player_start_pos_x, player_start_pos_y)

        #Draw
        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()
        timePassed = clock.tick(60)
        dt = timePassed / 1000

if __name__ == "__main__":
    main()
