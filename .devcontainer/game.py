import pygame
from planet import Planet
from fleet import Fleet
import random

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.planets = [
            Planet(200, 300, "player"),
            Planet(600, 300, "enemy")
        ]
        self.fleets = []
        self.selected = None

    def update(self):
        self.screen.fill((10, 10, 20))
        for planet in self.planets:
            planet.update()
            planet.draw(self.screen)

        # enviar flotas automáticas del enemigo
        if random.random() < 0.005:
            self.fleets.append(Fleet(600, 300, self.planets[0], "enemy"))

        # controles del jugador
        mouse = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        if mouse[0]:
            for p in self.planets:
                if (p.x - pos[0])**2 + (p.y - pos[1])**2 < p.radius**2:
                    self.selected = p
        elif mouse[2] and self.selected:
            for p in self.planets:
                if (p.x - pos[0])**2 + (p.y - pos[1])**2 < p.radius**2 and p != self.selected:
                    self.fleets.append(Fleet(self.selected.x, self.selected.y, p, "player"))
                    self.selected = None

        # actualizar flotas
        for fleet in self.fleets[:]:
            if fleet.update():
                self.fleets.remove(fleet)
            else:
                fleet.draw(self.screen)