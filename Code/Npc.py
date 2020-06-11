import pygame
import random


# 食物类, 用于提升坦克能力
class Npc(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		# 消灭当前所有敌人
		self.Npc_boom = './images/Npc/Npc_boom.png'
		# 当前所有敌人静止一段时间
		self.Npc_clock = './images/Npc/Npc_clock.png'
		# 使得坦克子弹可碎钢板
		self.Npc_gun = './images/Npc/Npc_gun.png'
		# 使得大本营的墙变为钢板
		self.Npc_iron = './images/Npc/Npc_gun.png'
		# 坦克获得一段时间的保护罩
		self.Npc_protect = './images/Npc/Npc_protect.png'
		# 坦克升级
		self.Npc_star = './images/Npc/Npc_star.png'
		# 坦克生命+1
		self.Npc_tank = './images/Npc/Npc_tank.png'
		# 所有食物
		self.Npcs = [self.Npc_boom, self.Npc_clock, self.Npc_gun, self.Npc_iron, self.Npc_protect, self.Npc_star, self.Npc_tank]
		self.kind = None
		self.Npc = None
		self.rect = None
		# 是否存在
		self.being = False
		# 存在时间
		self.time = 1000
	# 生成食物
	def generate(self):
		self.kind = random.randint(0, 6)
		self.Npc = pygame.image.load(self.Npcs[self.kind]).convert_alpha()
		self.rect = self.Npc.get_rect()
		self.rect.left, self.rect.top = random.randint(100, 500), random.randint(100, 500)
		self.being = True