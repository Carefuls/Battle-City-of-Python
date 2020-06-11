import sys
import pygame
import Map
import Bullet
import Npc
import Tanks
import Base
import datetime
from pygame.locals import *

def time2sec(y):
  h = y.hour
  m = y.minute
  s = y.second
  return int(h)*3600 + int(m)*60 + int(s)

# 开始界面显示
def show_start_interface(screen, width, height):
	tfont = pygame.font.Font('./font/Trans.ttf', width//7)
	cfont = pygame.font.Font('./font/Deng.ttf', width//21)
	title = tfont.render(u'Battle City', True, (182, 80, 17))
	content1 = cfont.render(u'1  单玩家模式', True, (248, 248, 248))
	content2 = cfont.render(u'2  双玩家模式', True, (248, 248, 248))
	content3 = cfont.render(u'3  查看历史成绩', True, (248, 248, 248))
	trect = title.get_rect()
	trect.midtop = (width/2, height/4)
	crect1 = content1.get_rect()
	crect1.midtop = (width/2, height/1.8)
	crect2 = content2.get_rect()
	crect2.midtop = (width/2, height/1.6)
	crect3 = content3.get_rect()
	crect3.midtop = (width/2, height/1.44)
	screen.blit(title, trect)
	screen.blit(content1, crect1)
	screen.blit(content2, crect2)
	screen.blit(content3, crect3)
	pygame.display.update()
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					return 1
				if event.key == pygame.K_2:
					return 2
				if event.key == pygame.K_3:
					with open("out.txt", "r") as f:
						print("玩家的历史成绩为:")
						data = f.read()
						print(data)



# 结束界面显示
def show_end_interface(screen, width, height, is_win):
	bg_img = pygame.image.load("./images/others/background.png")
	screen.blit(bg_img, (0, 0))
	if is_win:
		font = pygame.font.Font('./font/Trans.ttf', width//10)
		content = font.render(u'Congratulation!', True, (255, 0, 0))
		rect = content.get_rect()
		rect.midtop = (width/2, height/2)
		screen.blit(content, rect)
	else:
		fail_img = pygame.image.load("./images/others/gameover.png")
		rect = fail_img.get_rect()
		rect.midtop = (width/2, height/2)
		screen.blit(fail_img, rect)
	pygame.display.update()

# 关卡切换
def show_switch_stage(screen, width, height, stage):
	bg_img = pygame.image.load("./images/others/background.png")
	screen.blit(bg_img, (0, 0))
	font = pygame.font.Font('./font/Trans.ttf', width//14)
	content = font.render(u'STAGE  %d' % stage, True, (255, 255, 255))
	rect = content.get_rect()
	rect.midtop = (width/2, height/2)
	screen.blit(content, rect)
	pygame.display.update()
	delay_event = pygame.constants.USEREVENT
	pygame.time.set_timer(delay_event, 1000)
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			if event.type == delay_event:
				return


# 主函数
def main():
	# 初始化
	pygame.init()
	pygame.mixer.init()
	screen = pygame.display.set_mode((630, 630))
	pygame.display.set_caption("Battle City of Python")
	# 加载图片
	bg_img = pygame.image.load("./images/others/background.png")
	# 加载音效
	add_sound = pygame.mixer.Sound("./audios/add.wav")
	add_sound.set_volume(1)
	bang_sound = pygame.mixer.Sound("./audios/bang.wav")
	bang_sound.set_volume(1)
	blast_sound = pygame.mixer.Sound("./audios/blast.wav")
	blast_sound.set_volume(1)
	fire_sound = pygame.mixer.Sound("./audios/fire.wav")
	fire_sound.set_volume(1)
	Gunfire_sound = pygame.mixer.Sound("./audios/Gunfire.wav")
	Gunfire_sound.set_volume(1)
	hit_sound = pygame.mixer.Sound("./audios/hit.wav")
	hit_sound.set_volume(1)
	start_sound = pygame.mixer.Sound("./audios/start.wav")
	start_sound.set_volume(1)
	# 开始界面
	num_player = show_start_interface(screen, 630, 630)
	a = input("请输入尊姓大名：")
	doc = open('out.txt', 'a')
	print(a, file = doc)
	# 播放游戏开始的音乐
	start_sound.play()
	starttime = datetime.datetime.now()
	# 关卡
	stage = 0
	num_stage = 2
	# 游戏是否结束
	is_gameover = False
	# 时钟
	clock = pygame.time.Clock()
	# 主循环
	while not is_gameover:
		# 关卡
		stage += 1
		if stage > num_stage:
			break
		show_switch_stage(screen, 630, 630, stage)
		# 该关卡坦克总数量
		enemyTanks_total = min(stage * 18, 80)
		# 场上存在的敌方坦克总数量
		enemyTanks_now = 0
		# 场上可以存在的敌方坦克总数量
		enemyTanks_now_max = min(max(stage * 2, 4), 8)
		# 精灵组
		TanksGroup = pygame.sprite.Group()
		myTanksGroup = pygame.sprite.Group()
		enemyTanksGroup = pygame.sprite.Group()
		BulletsGroup = pygame.sprite.Group()
		myBulletsGroup = pygame.sprite.Group()
		enemyBulletsGroup = pygame.sprite.Group()
		myNpcsGroup = pygame.sprite.Group()
		# 自定义事件
		# 	-生成敌方坦克事件
		genEnemyEvent = pygame.constants.USEREVENT
		pygame.time.set_timer(genEnemyEvent, 100)
		# 	-敌方坦克静止恢复事件
		recoverEnemyEvent = pygame.constants.USEREVENT
		pygame.time.set_timer(recoverEnemyEvent, 8000)
		# 	-我方坦克无敌恢复事件
		noprotectMytankEvent = pygame.constants.USEREVENT
		pygame.time.set_timer(noprotectMytankEvent, 8000)
		# 关卡地图
		map_stage = Map.Map(stage)
		# 我方坦克
		tank_player1 = Tanks.myTank(1)
		TanksGroup.add(tank_player1)
		myTanksGroup.add(tank_player1)
		if num_player > 1:
			tank_player2 = Tanks.myTank(2)
			TanksGroup.add(tank_player2)
			myTanksGroup.add(tank_player2)
		is_switch_tank = True
		player1_moving = False
		player2_moving = False
		# 为了轮胎的动画效果
		time = 0
		# 敌方坦克
		for i in range(0, 3):
			if enemyTanks_total > 0:
				enemytank = Tanks.enemyTank(i)
				TanksGroup.add(enemytank)
				enemyTanksGroup.add(enemytank)
				enemyTanks_now += 1
				enemyTanks_total -= 1
		# 基地
		myBase = Base.Base()
		# 出场特效
		appearance_img = pygame.image.load("./images/others/appear.png").convert_alpha()
		appearances = []
		appearances.append(appearance_img.subsurface((0, 0), (48, 48)))
		appearances.append(appearance_img.subsurface((48, 0), (48, 48)))
		appearances.append(appearance_img.subsurface((96, 0), (48, 48)))
		# 关卡主循环
		while True:
			if is_gameover is True:
				break
			if enemyTanks_total < 1 and enemyTanks_now < 1:
				is_gameover = False
				break
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == genEnemyEvent:
					if enemyTanks_total > 0:
						if enemyTanks_now < enemyTanks_now_max:
							enemytank = Tanks.enemyTank()
							if not pygame.sprite.spritecollide(enemytank, TanksGroup, False, None):
								TanksGroup.add(enemytank)
								enemyTanksGroup.add(enemytank)
								enemyTanks_now += 1
								enemyTanks_total -= 1
				if event.type == recoverEnemyEvent:
					for each in enemyTanksGroup:
						each.can_move = True
				if event.type == noprotectMytankEvent:
					for each in myTanksGroup:
						myTanksGroup.protected = False
			# 检查用户键盘操作
			key_pressed = pygame.key.get_pressed()
			# 玩家一
			# WSAD -> 上下左右
			# 空格键射击
			if key_pressed[pygame.K_w]:
				TanksGroup.remove(tank_player1)
				tank_player1.move_up(TanksGroup, map_stage.brickGroup, map_stage.ironGroup, myBase)
				TanksGroup.add(tank_player1)
				player1_moving = True
			elif key_pressed[pygame.K_s]:
				TanksGroup.remove(tank_player1)
				tank_player1.move_down(TanksGroup, map_stage.brickGroup, map_stage.ironGroup, myBase)
				TanksGroup.add(tank_player1)
				player1_moving = True
			elif key_pressed[pygame.K_a]:
				TanksGroup.remove(tank_player1)
				tank_player1.move_left(TanksGroup, map_stage.brickGroup, map_stage.ironGroup, myBase)
				TanksGroup.add(tank_player1)
				player1_moving = True
			elif key_pressed[pygame.K_d]:
				TanksGroup.remove(tank_player1)
				tank_player1.move_right(TanksGroup, map_stage.brickGroup, map_stage.ironGroup, myBase)
				TanksGroup.add(tank_player1)
				player1_moving = True
			elif key_pressed[pygame.K_SPACE]:
				if not tank_player1.Bullet.being:
					fire_sound.play()
					tank_player1.shoot()
			elif key_pressed[pygame.K_ESCAPE]:
				endtime = datetime.datetime.now()
				runtime = endtime - starttime
				print(runtime)
				print(runtime, ' Quit', file = doc)
				doc.close()
				sys.exit()
			# 玩家二
			# ↑↓←→ -> 上下左右
			# 小键盘0键射击
			if num_player > 1:
				if key_pressed[pygame.K_UP]:
					TanksGroup.remove(tank_player2)
					tank_player2.move_up(TanksGroup, map_stage.brickGroup, map_stage.ironGroup, myBase)
					TanksGroup.add(tank_player2)
					player2_moving = True
				elif key_pressed[pygame.K_DOWN]:
					TanksGroup.remove(tank_player2)
					tank_player2.move_down(TanksGroup, map_stage.brickGroup, map_stage.ironGroup, myBase)
					TanksGroup.add(tank_player2)
					player2_moving = True
				elif key_pressed[pygame.K_LEFT]:
					TanksGroup.remove(tank_player2)
					tank_player2.move_left(TanksGroup, map_stage.brickGroup, map_stage.ironGroup, myBase)
					TanksGroup.add(tank_player2)
					player2_moving = True
				elif key_pressed[pygame.K_RIGHT]:
					TanksGroup.remove(tank_player2)
					tank_player2.move_right(TanksGroup, map_stage.brickGroup, map_stage.ironGroup, myBase)
					TanksGroup.add(tank_player2)
					player2_moving = True
				elif key_pressed[pygame.K_KP0]:
					if not tank_player2.Bullet.being:
						fire_sound.play()
						tank_player2.shoot()
				elif key_pressed[pygame.K_ESCAPE]:
					endtime = datetime.datetime.now()
					runtime = endtime - starttime
					print(runtime)
					print(runtime, ' Quit', file = doc)
					doc.close()
					sys.exit()
			# 背景
			screen.blit(bg_img, (0, 0))
			# 石头墙
			for each in map_stage.brickGroup:
				screen.blit(each.brick, each.rect)
			# 钢墙
			for each in map_stage.ironGroup:
				screen.blit(each.iron, each.rect)
			# 冰
			for each in map_stage.iceGroup:
				screen.blit(each.ice, each.rect)
			# 河流
			for each in map_stage.riverGroup:
				screen.blit(each.river, each.rect)
			# 树
			for each in map_stage.treeGroup:
				screen.blit(each.tree, each.rect)
			time += 1
			if time == 5:
				time = 0
				is_switch_tank = not is_switch_tank
			# 我方坦克
			if tank_player1 in myTanksGroup:
				if is_switch_tank and player1_moving:
					screen.blit(tank_player1.tank_0, (tank_player1.rect.left, tank_player1.rect.top))
					player1_moving = False
				else:
					screen.blit(tank_player1.tank_1, (tank_player1.rect.left, tank_player1.rect.top))
				if tank_player1.protected:
					screen.blit(tank_player1.protected_mask1, (tank_player1.rect.left, tank_player1.rect.top))
			if num_player > 1:
				if tank_player2 in myTanksGroup:
					if is_switch_tank and player2_moving:
						screen.blit(tank_player2.tank_0, (tank_player2.rect.left, tank_player2.rect.top))
						player1_moving = False
					else:
						screen.blit(tank_player2.tank_1, (tank_player2.rect.left, tank_player2.rect.top))
					if tank_player2.protected:
						screen.blit(tank_player1.protected_mask1, (tank_player2.rect.left, tank_player2.rect.top))
			# 敌方坦克
			for each in enemyTanksGroup:
				# 出生特效
				if each.born:
					if each.times > 0:
						each.times -= 1
						if each.times <= 10:
							screen.blit(appearances[2], (3+each.x*12*24, 3))
						elif each.times <= 20:
							screen.blit(appearances[1], (3+each.x*12*24, 3))
						elif each.times <= 30:
							screen.blit(appearances[0], (3+each.x*12*24, 3))
						elif each.times <= 40:
							screen.blit(appearances[2], (3+each.x*12*24, 3))
						elif each.times <= 50:
							screen.blit(appearances[1], (3+each.x*12*24, 3))
						elif each.times <= 60:
							screen.blit(appearances[0], (3+each.x*12*24, 3))
						elif each.times <= 70:
							screen.blit(appearances[2], (3+each.x*12*24, 3))
						elif each.times <= 80:
							screen.blit(appearances[1], (3+each.x*12*24, 3))
						elif each.times <= 90:
							screen.blit(appearances[0], (3+each.x*12*24, 3))
					else:
						each.born = False
				else:
					if is_switch_tank:
						screen.blit(each.tank_0, (each.rect.left, each.rect.top))
					else:
						screen.blit(each.tank_1, (each.rect.left, each.rect.top))
					if each.can_move:
						TanksGroup.remove(each)
						each.move(TanksGroup, map_stage.brickGroup, map_stage.ironGroup, myBase)
						TanksGroup.add(each)
			# 我方子弹
			for tank_player in myTanksGroup:
				if tank_player.Bullet.being:
					tank_player.Bullet.move()
					screen.blit(tank_player.Bullet.Bullet, tank_player.Bullet.rect)
					# 子弹碰撞敌方子弹
					for each in enemyBulletsGroup:
						if each.being:
							if pygame.sprite.collide_rect(tank_player.Bullet, each):
								tank_player.Bullet.being = False
								each.being = False
								enemyBulletsGroup.remove(each)
								break
						else:
							enemyBulletsGroup.remove(each)	
					# 子弹碰撞敌方坦克
					for each in enemyTanksGroup:
						if each.being:
							if pygame.sprite.collide_rect(tank_player.Bullet, each):
								if each.is_red == True:
									myNpc = Npc.Npc()
									myNpc.generate()
									myNpcsGroup.add(myNpc)
									each.is_red = False
								each.blood -= 1
								each.color -= 1
								if each.blood < 0:
									bang_sound.play()
									each.being = False
									enemyTanksGroup.remove(each)
									enemyTanks_now -= 1
									TanksGroup.remove(each)
								else:
									each.reload()
								tank_player.Bullet.being = False
								break
						else:
							enemyTanksGroup.remove(each)
							TanksGroup.remove(each)
					# 子弹碰撞石头墙
					if pygame.sprite.spritecollide(tank_player.Bullet, map_stage.brickGroup, True, None):
						tank_player.Bullet.being = False
					# 子弹碰钢墙
					if tank_player.Bullet.stronger:
						if pygame.sprite.spritecollide(tank_player.Bullet, map_stage.ironGroup, True, None):
							tank_player.Bullet.being = False
					else:
						if pygame.sprite.spritecollide(tank_player.Bullet, map_stage.ironGroup, False, None):
							tank_player.Bullet.being = False
					# 子弹碰基地
					if pygame.sprite.collide_rect(tank_player.Bullet, myBase):
						tank_player.Bullet.being = False
						myBase.set_dead()
						is_gameover = True
			# 敌方子弹
			for each in enemyTanksGroup:
				if each.being:
					if each.can_move and not each.Bullet.being:
						enemyBulletsGroup.remove(each.Bullet)
						each.shoot()
						enemyBulletsGroup.add(each.Bullet)
					if not each.born:
						if each.Bullet.being:
							each.Bullet.move()
							screen.blit(each.Bullet.Bullet, each.Bullet.rect)
							# 子弹碰撞我方坦克
							for tank_player in myTanksGroup:
								if pygame.sprite.collide_rect(each.Bullet, tank_player):
									if not tank_player.protected:
										bang_sound.play()
										tank_player.life -= 1
										if tank_player.life < 0:
											myTanksGroup.remove(tank_player)
											TanksGroup.remove(tank_player)
											if len(myTanksGroup) < 1:
												is_gameover = True
										else:
											tank_player.reset()
									each.Bullet.being = False
									enemyBulletsGroup.remove(each.Bullet)
									break
							# 子弹碰撞石头墙
							if pygame.sprite.spritecollide(each.Bullet, map_stage.brickGroup, True, None):
								each.Bullet.being = False
								enemyBulletsGroup.remove(each.Bullet)
							# 子弹碰钢墙
							if each.Bullet.stronger:
								if pygame.sprite.spritecollide(each.Bullet, map_stage.ironGroup, True, None):
									each.Bullet.being = False
							else:
								if pygame.sprite.spritecollide(each.Bullet, map_stage.ironGroup, False, None):
									each.Bullet.being = False
							# 子弹碰基地
							if pygame.sprite.collide_rect(each.Bullet, myBase):
								each.Bullet.being = False
								myBase.set_dead()
								is_gameover = True
				else:
					enemyTanksGroup.remove(each)
					TanksGroup.remove(each)
			# 家
			screen.blit(myBase.Base, myBase.rect)
			# 食物
			for myNpc in myNpcsGroup:
				if myNpc.being and myNpc.time > 0:
					screen.blit(myNpc.Npc, myNpc.rect)
					myNpc.time -= 1
					for tank_player in myTanksGroup:
						if pygame.sprite.collide_rect(tank_player, myNpc):
							# 消灭当前所有敌人
							if myNpc.kind == 0:
								for _ in enemyTanksGroup:
									bang_sound.play()
								enemyTanksGroup = pygame.sprite.Group()
								enemyTanks_total -= enemyTanks_now
								enemyTanks_now = 0
							# 敌人静止
							if myNpc.kind == 1:
								for each in enemyTanksGroup:
									each.can_move = False
							# 子弹增强
							if myNpc.kind == 2:
								add_sound.play()
								tank_player.Bullet.stronger = True
							# 使得基地的墙变为钢板
							if myNpc.kind == 3:
								map_stage.protect_Base()
							# 坦克获得一段时间的保护罩
							if myNpc.kind == 4:
								add_sound.play()
								for tank_player in myTanksGroup:
									tank_player.protected = True
							# 坦克升级
							if myNpc.kind == 5:
								add_sound.play()
								tank_player.up_level()
							# 坦克生命+1
							if myNpc.kind == 6:
								add_sound.play()
								tank_player.life += 1
							myNpc.being = False
							myNpcsGroup.remove(myNpc)
							break
				else:
					myNpc.being = False
					myNpcsGroup.remove(myNpc)
			pygame.display.flip()
			clock.tick(60)
	if not is_gameover:
		show_end_interface(screen, 630, 630, True)
		endtime = datetime.datetime.now()
		runtime = endtime - starttime
		print(runtime)
		print(runtime, ' Win', file = doc)
		doc.close()
	else:
		show_end_interface(screen, 630, 630, False)
		endtime = datetime.datetime.now()
		runtime = endtime - starttime
		print(runtime)
		print(runtime, ' Fail', file = doc)
		doc.close()

if __name__ == '__main__':
	main()
