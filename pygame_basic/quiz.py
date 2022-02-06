#pip install pygame
import pygame
import random
####################################################
pygame.init() #기본 초기화(필수)

# 화면 크기
screen_width=480
screen_height=640
screen=pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("quiz")

#FPS
clock=pygame.time.Clock()
####################################################

#1 사용자 게임 초기화 (배경, 이미지, 좌표, 폰트, 속도...)
background=pygame.image.load("C:/Users/bini3/Desktop/pygame_basic/background.png")

character=pygame.image.load("C:/Users/bini3/Desktop/pygame_basic/character.png")
character_size=character.get_rect().size
character_width=character_size[0]
character_height=character_size[1]
character_x_pos=(screen_width-character_width)/2
character_y_pos=screen_height-character_height

to_x=0
to_y=0
character_speed=0.6

enemy=pygame.image.load("C:/Users/bini3/Desktop/pygame_basic/enemy.png")
enemy_size=enemy.get_rect().size
enemy_width=enemy_size[0]
enemy_height=enemy_size[1]
enemy_x_pos=random.randint(0,screen_width)
enemy_y_pos=0
e_to_x=0
e_to_y=0
enemy_speed=0.6


####################################################
running=True
while running:
    dt=clock.tick(30) #FPS설정
####################################################

#2 이벤트 처리 (키보드, 마우스...)

####################################################
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                to_x-=character_speed
            elif event.key==pygame.K_RIGHT:
                to_x+=character_speed
                
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                to_x=0
                
        #while enemy_y_pos == -screen_height:
        #   e_to_y+=enemy_speed
        #   if enemy_y_pos==screen_height:
        #       enemy_x_pos=random.randint(0,screen_width)
        #       enemy_y_pos=0

####################################################

#3 게임 캐릭터 위치 정의
    character_x_pos += to_x*dt
    character_y_pos += to_y*dt
    
    if character_x_pos<0:
        character_x_pos=0
    elif character_x_pos>screen_width-character_width:
        character_x_pos=screen_width-character_width
    
    enemy_x_pos+=e_to_x*dt
    enemy_y_pos+=e_to_y*dt
        
    if enemy_x_pos<0:
        enemy_x_pos=0
    elif enemy_x_pos>screen_width-enemy_width:
        enemy_x_pos=screen_width=enemy_width
               

#4 충돌 처리
    character_rect=character.get_rect()
    character_rect.left=character_x_pos
    character_rect.top=character_y_pos

    enemy_rect=enemy.get_rect()
    enemy_rect.left=enemy_x_pos
    enemy_rect.top=enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌했습니다")
        running=False

#5 화면 그리기
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos, enemy_y_pos))

####################################################
    pygame.display.update()
####################################################

pygame.quit()