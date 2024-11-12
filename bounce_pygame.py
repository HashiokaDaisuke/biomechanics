import random
import pygame
import math


class Particle:
    def __init__(self, init_pos, vel, theta,r):
        self.is_alive = True
        self.x, self.y = 0,0
        self.init_x, self.init_y = init_pos
        self.v = vel
        self.theta = theta
        self.r = r

    def update(self, width, height, dt, g):
        self.g_theta = - g * math.sin(math.radians(self.theta))
        self.v += self.g_theta * dt
        self.theta += self.v / self.r * 180 / math.pi
        self.x = self.init_x + self.r * math.sin(math.radians(self.theta))
        self.y = self.init_y - self.r * (1 - math.cos(math.radians(self.theta)))
        if self.x < 0 or self.x > width or self.y > height:
            self.is_alive = False

    def draw(self, screen):
        radius = 10
        pygame.draw.circle(screen, pygame.Color("green"), (self.x, self.y), radius)


def main():
    pygame.init()
    width, height = 600, 400
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    dt = 1.0
    g = 0.5
    theta = -90
    r = 100
    v = 0
    particle_list = []

    while True:
        frames_per_second = 60
        clock.tick(frames_per_second)

        should_quit = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                should_quit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    should_quit = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    p = Particle((150,350), v, theta ,r)
                    particle_list.append(p)
        if should_quit:
            break

        for p in particle_list:
            p.update(width, height, dt, g)

        particle_list[:] = [p for p in particle_list if p.is_alive]

        screen.fill(pygame.Color("black"))
        for p in particle_list:
            p.draw(screen)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()