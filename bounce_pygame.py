import random
import pygame
import math


class Particle:
    def __init__(self, init_pos, r, theta_cut):
        self.is_alive = True
        self.x, self.y = 0,0
        self.init_x, self.init_y = init_pos
        self.v, self.vx, self.vy = 0, 0, 0
        self.theta = -90 #[deg]
        self.r = r
        self.theta_cut = theta_cut

    def update(self, width, height, dt, g):
        if self.theta < self.theta_cut:
            self.g_theta = - g * math.sin(math.radians(self.theta))
            self.v += self.g_theta * dt
            self.theta += self.v / self.r * 180 / math.pi * dt
            self.x = self.init_x + self.r * math.sin(math.radians(self.theta))
            self.y = self.init_y - self.r * (1 - math.cos(math.radians(self.theta)))
            self.vx = self.v * math.cos(math.radians(self.theta))
            self.vy = -self.v * math.sin(math.radians(self.theta))
        else:
            self.vy += g * dt
            self.x += self.vx * dt
            self.y += self.vy * dt
            self.v += self.g_theta * dt
        if self.x < 0 or self.x > width or self.y > self.init_y:
            self.is_alive = False

    def draw(self, screen):
        radius = 4
        pygame.draw.circle(screen, pygame.Color("green"), (self.x, self.y), radius)


def main():
    pygame.init()
    width, height = 600, 400
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    dt = 0.4
    g = 0.5
    r = 100
    theta_cut = 40.9853
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

                    p = Particle((150,350), r, theta_cut)
                    particle_list.append(p)
        if should_quit:
            break

        for p in particle_list:
            p.update(width, height, dt, g)

        particle_list[:] = [p for p in particle_list if p.is_alive]

        screen.fill(pygame.Color("black"))
        pygame.draw.line(screen, (0,95,0), (150,250), (150,350), 2)
        pygame.draw.line(screen, (0,95,0), (0,350), (600,350), 2)
        pygame.draw.arc(screen, (0,95,0),(50,150,200,200), math.radians(180), math.radians(270 + theta_cut), 1)
        for p in particle_list:
            p.draw(screen)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()