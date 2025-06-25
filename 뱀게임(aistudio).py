import pygame
import sys
import random
import time

# 게임 초기화
pygame.init()

# 화면 크기 설정
screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('파이썬 뱀 게임')

# 색상 정의 (RGB)
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)

# 게임 속도 제어
clock = pygame.time.Clock()
snake_speed = 15

# 뱀 초기 위치 및 크기
snake_position = [100, 50]
# 뱀은 여러 개의 사각형으로 이루어지므로 리스트로 몸통을 표현
snake_body = [[100, 50], [90, 50], [80, 50]]
block_size = 10

# 먹이 초기 위치
food_position = [random.randrange(1, (screen_width//block_size)) * block_size,
                 random.randrange(1, (screen_height//block_size)) * block_size]
food_spawn = True

# 뱀 초기 방향
direction = 'RIGHT'
change_to = direction

# 점수
score = 0

# 게임 오버 함수
def game_over():
    font = pygame.font.SysFont('malgungothic', 50) # 'malgungothic' or 'tahoma'
    game_over_surface = font.render('게임 오버!', True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (screen_width/2, screen_height/4)
    
    screen.blit(game_over_surface, game_over_rect)
    show_score(0, RED, 'malgungothic', 20)
    pygame.display.flip()
    
    time.sleep(2) # 2초 대기
    pygame.quit()
    sys.exit()

# 점수 표시 함수
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('점수 : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (70, 10)
    else:
        score_rect.midtop = (screen_width/2, screen_height/1.25)
    
    screen.blit(score_surface, score_rect)

# 메인 게임 루프
while True:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 키보드 방향키 입력 처리
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
                
    # 뱀이 자기 자신과 부딪히는 것을 방지
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
        
    # 뱀 이동
    if direction == 'UP':
        snake_position[1] -= block_size
    if direction == 'DOWN':
        snake_position[1] += block_size
    if direction == 'LEFT':
        snake_position[0] -= block_size
    if direction == 'RIGHT':
        snake_position[0] += block_size
        
    # 뱀 몸통 성장 (새로운 머리 위치를 몸통 리스트의 맨 앞에 추가)
    snake_body.insert(0, list(snake_position))
    
    # 뱀이 먹이를 먹었는지 확인
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 10
        food_spawn = False
    else:
        # 먹이를 먹지 않았다면, 몸통의 마지막 부분을 제거하여 길이를 유지
        snake_body.pop()
        
    # 먹이가 없다면 새로 생성
    if not food_spawn:
        food_position = [random.randrange(1, (screen_width//block_size)) * block_size,
                         random.randrange(1, (screen_height//block_size)) * block_size]
    food_spawn = True
    
    # 화면 그리기
    screen.fill(BLACK)
    
    # 뱀 그리기
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], block_size, block_size))
        
    # 먹이 그리기
    pygame.draw.rect(screen, WHITE, pygame.Rect(food_position[0], food_position[1], block_size, block_size))
    
    # 벽에 부딪혔을 때 게임 오버 처리
    if snake_position[0] < 0 or snake_position[0] > screen_width-block_size:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > screen_height-block_size:
        game_over()
        
    # 자기 자신과 부딪혔을 때 게임 오버 처리
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
            
    # 점수 표시
    show_score(1, WHITE, 'consolas', 20)
    
    # 화면 업데이트
    pygame.display.update()
    
    # 게임 속도 조절
    clock.tick(snake_speed)