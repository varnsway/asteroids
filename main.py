import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Asteroid.containers = (asteroids, updatable, drawable)
Player.containers = (updatable, drawable)
Shot.containers = (shots,)
AsteroidField.containers = (updatable)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0    
    p = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    af = AsteroidField()
    

    while True:
        screen.fill("black")
        for u in updatable:
            u.update(dt)
            p.cd_timer -= dt
        shots.update(dt)
        for a in asteroids:
            if a.colide(p):
                print("Gamer over!")
                return
        for a in asteroids:
            for s in shots:
                if a.colide(s):
                    a.split()
                    s.kill()
        for d in drawable:
            d.draw(screen)
        for s in shots:
            s.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()