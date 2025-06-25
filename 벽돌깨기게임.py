#설치
#pip install pygame
import pygame
import sys

# 초기화
pygame.init()

# 화면 크기
WIDTH, HEIGHT = 480, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("벽돌깨기 게임")

# 색상
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BRICK_COLOR = (200, 0, 0)
PADDLE_COLOR = (0, 120, 255)
BALL_COLOR = (0, 255, 120)

# 패들
PADDLE_WIDTH, PADDLE_HEIGHT = 80, 15
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_speed = 7

# 공
BALL_RADIUS = 10
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_dx, ball_dy = 4, -4

# 벽돌
BRICK_ROWS, BRICK_COLS = 5, 8
BRICK_WIDTH = WIDTH // BRICK_COLS
BRICK_HEIGHT = 30
bricks = []
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        brick = pygame.Rect(col * BRICK_WIDTH, row * BRICK_HEIGHT + 40, BRICK_WIDTH - 2, BRICK_HEIGHT - 2)
        bricks.append(brick)

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed

    # 공 이동
    ball.x += ball_dx
    ball.y += ball_dy

    # 벽 충돌
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_dx = -ball_dx
    if ball.top <= 0:
        ball_dy = -ball_dy
    if ball.bottom >= HEIGHT:
        print("Game Over!")
        running = False

    # 패들 충돌
    if ball.colliderect(paddle):
        ball_dy = -ball_dy

    # 벽돌 충돌
    hit_index = ball.collidelist(bricks)
    if hit_index != -1:
        del bricks[hit_index]
        ball_dy = -ball_dy

    # 화면 그리기
    screen.fill(BLACK)
    pygame.draw.rect(screen, PADDLE_COLOR, paddle)
    pygame.draw.ellipse(screen, BALL_COLOR, ball)
    for brick in bricks:
        pygame.draw.rect(screen, BRICK_COLOR, brick)
    pygame.display.flip()

    # 승리 조건
    if not bricks:
        print("You Win!")
        running = False