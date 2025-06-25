# 뱀게임.py
# pip install pygame 필요

import pygame
import random
import sys

# 초기화
pygame.init()

# 화면 크기
WIDTH, HEIGHT = 480, 480
CELL_SIZE = 20
COLS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("뱀 게임")

# 색상
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 뱀, 사과 초기화
snake = [(COLS // 2, ROWS // 2)]
direction = (0, -1)  # 위로 시작
apple = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))

clock = pygame.time.Clock()
running = True

def draw():
    screen.fill(BLACK)
    # 뱀 그리기
    for x, y in snake:
        pygame.draw.rect(screen, GREEN, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    # 사과 그리기
    ax, ay = apple
    pygame.draw.rect(screen, RED, (ax * CELL_SIZE, ay * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.flip()

def move_snake():
    head_x, head_y = snake[0]
    dx, dy = direction
    new_head = (head_x + dx, head_y + dy)
    return new_head

while running:
    clock.tick(10)  # FPS
    next_direction = direction  # 방향 임시 저장
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                next_direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                next_direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                next_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                next_direction = (1, 0)

    direction = next_direction  # 한 번만 방향 변경

    new_head = move_snake()

    # 벽 또는 자기 몸에 부딪히면 게임 오버
    if (new_head[0] < 0 or new_head[0] >= COLS or
        new_head[1] < 0 or new_head[1] >= ROWS or
        new_head in snake):
        print("Game Over!")
        running = False
        continue

    snake.insert(0, new_head)

    # 사과 먹으면 길이 증가, 아니면 꼬리 제거
    if new_head == apple:
        while True:
            apple = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
            if apple not in snake:
                break
    else:
        snake.pop()

    draw()

pygame.quit()
sys.exit()