import pygame
import math

class Fleet:
    def __init__(self, x, y, target, owner):
        self.x = x
        self.y = y
        self.target = target
        self.owner = owner
        self.speed = 2.5
        self.ships = 10
        self.color = (0, 255, 0) if owner == "player" else (255, 0, 0)

    def update(self):
        dx = self.target.x - self.x
        dy = self.target.y - self.y
        dist = math.hypot(dx, dy)
        if dist > 1:
            self.x += self.speed * dx / dist
            self.y += self.speed * dy / dist
        else:
            # llegada
            self.target.ships += self.ships if self.owner == self.target.owner else -self.ships
            return True  # eliminar flota
        return False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 5)