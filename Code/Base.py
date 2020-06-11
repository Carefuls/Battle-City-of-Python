import pygame
# 基地类
class Base(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.Bases = ['./images/Base/Base1.png', './images/Base/Base2.png', './images/Base/Base_destroyed.png']
		self.Base = pygame.image.load(self.Bases[0])
		self.rect = self.Base.get_rect()
		self.rect.left, self.rect.top = (3 + 12 * 24, 3 + 24 * 24)
		self.alive = True
	# 基地置为摧毁状态
	def set_dead(self):
		self.Base = pygame.image.load(self.Bases[-1])
		self.alive = False