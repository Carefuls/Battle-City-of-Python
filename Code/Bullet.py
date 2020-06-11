import pygame


# 子弹类
class Bullet(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		# 子弹四个方向(上下左右)
		self.Bullets = ['./images/Bullet/Bullet_up.png', './images/Bullet/Bullet_down.png', './images/Bullet/Bullet_left.png', './images/Bullet/Bullet_right.png']
		# 子弹方向(默认向上)
		self.direction_x, self.direction_y = 0, -1
		self.Bullet = pygame.image.load(self.Bullets[0])
		self.rect = self.Bullet.get_rect()
		# 在坦克类中再赋实际值
		self.rect.left, self.rect.right = 0, 0
		# 速度
		self.speed = 6
		# 是否存活
		self.being = False
		# 是否为加强版子弹(可碎钢板)
		self.stronger = False
	# 改变子弹方向
	def turn(self, direction_x, direction_y):
		self.direction_x, self.direction_y = direction_x, direction_y
		if self.direction_x == 0 and self.direction_y == -1:
			self.Bullet = pygame.image.load(self.Bullets[0])
		elif self.direction_x == 0 and self.direction_y == 1:
			self.Bullet = pygame.image.load(self.Bullets[1])
		elif self.direction_x == -1 and self.direction_y == 0:
			self.Bullet = pygame.image.load(self.Bullets[2])
		elif self.direction_x == 1 and self.direction_y == 0:
			self.Bullet = pygame.image.load(self.Bullets[3])
		else:
			raise ValueError('Bullet class -> direction value error.')
	# 移动
	def move(self):
		self.rect = self.rect.move(self.speed*self.direction_x, self.speed*self.direction_y)
		# 到地图边缘后消失
		if (self.rect.top < 3) or (self.rect.bottom > 630 - 3) or (self.rect.left < 3) or (self.rect.right > 630 - 3):
			self.being = False