
import pygame
from math import sin, cos, radians

#colors
RED = (255, 0, 0)

class Player(pygame.sprite.Sprite):
	def __init__(self, screen_width, screen_height):
		super(Player, self).__init__()
		#self.image = pygame.Surface([20, 20])
		#self.image.fill(RED)
		self.image = pygame.image.load("doggo2.png")
		self.rect = self.image.get_rect()
		self.vel = 0
		self.angle = 0
		self.max_w = screen_width
		self.max_h = screen_height
		self.rect.x = 200
		self.rect.y = 200

	def update(self, angle):
		self.rect.x += self.vel * sin(radians(angle))
		if self.rect.x >= self.max_w:
			self.rect.x %= self.max_w
		elif self.rect.x <= 0:
			self.rect.x = self.max_w
		self.rect.y -= self.vel * cos(radians(angle))
		if self.rect.y >= self.max_h:
			self.rect.y %= self.max_h
		elif self.rect.y <= 0:
			self.rect.y = self.max_h
