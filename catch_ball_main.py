#!-*-coding:utf-8-*-
# !@Date: 2018/7/28 17:02
# !@Author: Liu Rui
# !@github: bigfoolliu


import pygame
from pygame import *
import sys
import time
import random


pygame.init()

game_window = pygame.display.set_mode((600, 500))

window_color = (0, 0, 255)
ball_color = (255, 165, 0)
rect_color = (255, 0, 0)

my_font = pygame.font.Font(None, 70)
score = 0

ball_x = random.randint(20, 580)
ball_y = 20

move_x = 1
move_y = 1

point = 1
count = 1

pygame.display.set_caption("接球小游戏")

while True:

	game_window.fill(window_color)

	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()

	mouse_x, mouse_y = pygame.mouse.get_pos()
	pygame.draw.circle(game_window, ball_color, (ball_x, ball_y), 20)
	pygame.draw.rect(game_window, rect_color, (mouse_x, 490, 100, 10))

	my_text = my_font.render(str(score), False, (255, 255, 255))
	game_window.blit(my_text, (500, 30))

	ball_x += move_x
	ball_y += move_y

	if ball_x <= 20 or ball_x >= 580:
		move_x = -move_x
	if ball_y <= 20:
		move_y = -move_y
	elif mouse_x - 20 < ball_x < mouse_x + 120 and ball_y >= 470:
		move_y = -move_y
		score += point
		count += 1
		if count == 3:
			count = 0
			point += point
			if move_x > 0:
				move_x += 1
			else:
				move_x -= 1
			move_y -= 1
	elif ball_y >= 480 and (ball_x <= move_x or ball_x >= move_x + 120):
		break

	pygame.display.update()

	time.sleep(0.005)
