import pygame
import random


# 砖墙
class Brick(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.brick = pygame.image.load('./images/Scene/brick.png')
		self.rect = self.brick.get_rect()
		self.being = False


# 钢墙
class Iron(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.iron = pygame.image.load('./images/Scene/iron.png')
		self.rect = self.iron.get_rect()
		self.being = False


# 冰
class Ice(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.ice = pygame.image.load('./images/Scene/ice.png')
		self.rect = self.ice.get_rect()
		self.being = False


# 河流
class River(pygame.sprite.Sprite):
	def __init__(self, kind=None):
		pygame.sprite.Sprite.__init__(self)
		if kind is None:
			self.kind = random.randint(0, 1)
		self.rivers = ['./images/Scene/river1.png', './images/Scene/river2.png']
		self.river = pygame.image.load(self.rivers[self.kind])
		self.rect = self.river.get_rect()
		self.being = False


# 树
class Tree(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.tree = pygame.image.load('./images/Scene/tree.png')
		self.rect = self.tree.get_rect()
		self.being = False


# 地图
class Map():
	def __init__(self, stage):
		self.brickGroup = pygame.sprite.Group()
		self.ironGroup  = pygame.sprite.Group()
		self.iceGroup = pygame.sprite.Group()
		self.riverGroup = pygame.sprite.Group()
		self.treeGroup = pygame.sprite.Group()
		if stage == 1:
			self.stage1()
		elif stage == 2:
			self.stage2()
	# 关卡一
	def stage1(self):
		for x in [5, 6, 7, 18, 19, 20]:
			for y in [0, 1, 2]:
				self.tree = Tree()
				self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24
				self.tree.being = True
				self.treeGroup.add(self.tree)
		for x, y in [(11, 4), (14, 4), (9, 11), (11, 11), (14, 11), (16, 11)]:
			self.tree = Tree()
			self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24
			self.tree.being = True
			self.treeGroup.add(self.tree)
		for x, y in [(12, 5), (13, 5)]:
			self.ice = Ice()
			self.ice.rect.left, self.ice.rect.top = 3 + x * 24, 3 + y * 24
			self.ice.being = True
			self.iceGroup.add(self.ice)
		for x in [5, 6, 12, 13, 19, 20]:
			for y in [3, 4]:
				self.ice = Ice()
				self.ice.rect.left, self.ice.rect.top = 3 + x * 24, 3 + y * 24
				self.ice.being = True
				self.iceGroup.add(self.ice)
		for x in [0, 1, 2, 3, 4, 10, 15, 21, 22, 23, 24, 25]:
			for y in [2]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x in [10, 15]:
			for y in [0, 1, 3, 4]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x, y in [(3, 3), (3, 4), (4, 4), (4, 5), (5, 5), (5, 6), (22, 3), (22, 4), (21, 4), (21, 5), (20, 5), (20, 6)]:
			self.brick = Brick()
			self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
			self.brick.being = True
			self.brickGroup.add(self.brick)
		for x in [10, 15]:
			for y in [0, 1, 3, 4]:
			    self.brick = Brick()
			    self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
			    self.brick.being = True
			    self.brickGroup.add(self.brick)
		for x in [0, 1, 2, 3, 4, 5, 20, 21, 22, 23, 24, 25]:
			for y in [8]:
			    self.brick = Brick()
			    self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
			    self.brick.being = True
			    self.brickGroup.add(self.brick)
		for x in [8, 9, 10, 11, 12, 13, 14, 15, 16, 17]:
			for y in [12]:
			    self.brick = Brick()
			    self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
			    self.brick.being = True
			    self.brickGroup.add(self.brick)
		for x, y in [(0, 13), (1, 13), (7, 12), (8, 11), (9, 10), (16, 10), (17, 11), (18, 12), (24, 13), (25, 13), (12, 6), (12, 7), (13, 6), (13, 7)]:
			self.iron = Iron()
			self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
			self.iron.being = True
			self.ironGroup.add(self.iron)
		for x in [11, 14]:
			for y in [14, 15, 16, 17, 18, 19]:
			    self.river = River()
			    self.river.rect.left, self.river.rect.top = 3 + x * 24, 3 + y * 24
			    self.river.being = True
			    self.riverGroup.add(self.river)
		for x in [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20]:
			for y in [19]:
			    self.river = River()
			    self.river.rect.left, self.river.rect.top = 3 + x * 24, 3 + y * 24
			    self.river.being = True
			    self.riverGroup.add(self.river)
		for x in [5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20]:
			for y in [20]:
			    self.brick = Brick()
			    self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
			    self.brick.being = True
			    self.brickGroup.add(self.brick)
		for x, y in [(3, 13), (22, 13), (0, 16), (25, 16), (12, 19), (13, 19), (11, 23), (11, 24), (11, 25), (12, 23), (13, 23), (14, 23), (14, 24), (14, 25), (5, 21), (5, 22), (6, 21), (6, 22), (19, 21), (19, 22), (20, 21), (20, 22)]:
			self.brick = Brick()
			self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
			self.brick.being = True
			self.brickGroup.add(self.brick)		
		for x in [3, 5, 6, 19, 20, 22]:
			for y in [16]:
			    self.brick = Brick()
			    self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
			    self.brick.being = True
			    self.brickGroup.add(self.brick)
		for x in [4, 21]:
			for y in [14, 15, 16, 17, 18]:
			    self.brick = Brick()
			    self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
			    self.brick.being = True
			    self.brickGroup.add(self.brick)
		for x in [5, 20]:
			for y in [23, 24, 25]:
			    self.iron = Iron()
			    self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
			    self.iron.being = True
			    self.ironGroup.add(self.iron)
		for x in [10, 11, 12, 13, 14, 15]:
			for y in [10]:
			    self.tree = Tree()
			    self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24
			    self.tree.being = True
			    self.treeGroup.add(self.tree)
	# 关卡二
	def stage2(self):
		for x in [1, 8, 12, 14, 22]:
			for y in [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x in [2, 3, 4]:
			for y in [7, 12, 17]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x in [9, 10, 11]:
			for y in [17]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x in [15, 16, 17]:
			for y in [7, 11]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x, y in [(20, 7), (21, 7), (23, 7), (24, 7), (5, 8), (6, 9), (6, 10), (5, 11), (5, 13), (6, 14), (6, 15), (5, 16), (18, 7), (18, 8), (18, 9), (18, 10), (18, 11)]:
			self.brick = Brick()
			self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
			self.brick.being = True
			self.brickGroup.add(self.brick)
		for x in [10, 12, 14, 16, 18]:
			for y in [1, 2, 3, 4, 5]:
			    self.ice = Ice()
			    self.ice.rect.left, self.ice.rect.top = 3 + x * 24, 3 + y * 24
			    self.ice.being = True
			    self.iceGroup.add(self.ice)
		for x in [10, 12, 16]:
			for y in [18, 19, 20, 21, 22]:
			    self.river = River()
			    self.river.rect.left, self.river.rect.top = 3 + x * 24, 3 + y * 24
			    self.river.being = True
			    self.riverGroup.add(self.river)
		for x, y in [(6, 1), (7, 1), (8, 1), (8, 2), (8, 3), (7, 3), (6, 3), (6, 4), (6, 5), (7, 5), (8, 5), (11, 1), (11, 5), (17, 1), (17, 3), (17, 5)]:
			self.ice = Ice()
			self.ice.rect.left, self.ice.rect.top = 3 + x * 24, 3 + y * 24
			self.ice.being = True
			self.iceGroup.add(self.ice)
		for x, y in [(6, 18), (7, 18), (8, 18), (6, 19), (6, 20), (7, 20), (8, 20), (8, 21), (8, 22), (7, 22), (6, 22), (13, 18), (14, 18), (13, 22), (14, 22), (17, 18), (18, 18), (17, 20), (18, 20), (17, 22), (18, 22)]:
			self.river = River()
			self.river.rect.left, self.river.rect.top = 3 + x * 24, 3 + y * 24
			self.river.being = True
			self.riverGroup.add(self.river)
		for x, y in [(0, 4), (1, 4), (12, 6), (13, 6), (24, 4), (25, 4), (5, 24), (5, 25), (20, 24), (20, 25), (0, 20), (1, 20), (24, 20), (25, 20)]:
			self.iron = Iron()
			self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
			self.iron.being = True
			self.ironGroup.add(self.iron)
		for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
			self.brick = Brick()
			self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
			self.brick.being = True
			self.brickGroup.add(self.brick)
		for x, y in [(0, 25), (1, 24), (2, 23), (3, 23), (3, 24), (3, 25), (22, 23), (22, 24), (22, 25), (23, 23), (24, 24), (25, 25)]:
			self.tree = Tree()
			self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24
			self.tree.being = True
			self.treeGroup.add(self.tree)

	def protect_home(self):
		for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
			self.iron = Iron()
			self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
			self.iron.being = True
			self.ironGroup.add(self.iron)
