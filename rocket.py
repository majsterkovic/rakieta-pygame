import pygame
from pygame.math import Vector2

class Rocket(object):

    def __init__(self, game):
        self.game = game

        self.pos = Vector2(0,0)
        self.vel = Vector2(0,0)
        self.acc = Vector2(0,0)

    def add_force(self, force):
        self.acc += force

    def tick(self):
        #input

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.add_force(Vector2(0,-1))
        if pressed[pygame.K_s]:
            self.add_force(Vector2(0,1))
        if pressed[pygame.K_a]:
            self.add_force(Vector2(-1,0))
        if pressed[pygame.K_d]:
            self.add_force(Vector2(1,0))

        #fizyka
        self.vel *= 0.8
        self.vel = Vector2(0, -1)

        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

    def draw(self):
        rect = pygame.Rect(self.pos.x, self.pos.y, 50, 50)
        pygame.draw.rect(self.game.screen, (100, 35, 115), rect)