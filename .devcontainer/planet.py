import pygame

class Planet:
    def __init__(self, x, y, owner):
        self.x = x
        self.y = y
        self.owner = owner
        self.ships = 50
        self.radius = 30
        self.color = (0, 200, 0) if owner == "player" else (200, 0, 0)

    def update(self):
        self.ships += 0.05  # crecimiento lento

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        font = pygame.font.SysFont(None, 20)
        text = font.render(str(int(self.ships)), True, (255, 255, 255))
        screen.blit(text, (self.x - 10, self.y - 10))