#pip install pygame 터미널에서 파이게임 설치
import pygame #잘 설치됐는지 확인

pygame.init() #필수(초기화)

#화면크기
screen_width=480 #가로
screen_height=640 #세로
screen=pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀
pygame.display.set_caption("for graphite") #게임 이름
#다음 명령이 없으면 창은 자동으로 꺼짐

#배경불러오기
background=pygame.image.load("C:/Users/bini3/Desktop/pygame_basic/background.png")

#캐릭터 불러오기
character=pygame.image.load("C:/Users/bini3/Desktop/pygame_basic/character.png")
character_size=character.get_rect().size
character_width=character_size[0]
character_height=character_size[1]
character_x_pos=screen_width/2-character_width/2
character_y_pos=screen_height-character_height

#이동할 좌표
to_x=0
to_y=0

#이벤트 루프
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN: #키가 눌렸다면
            if event.key==pygame.K_LEFT:
                to_x-=3 #to_x=to_x-5
            elif event.key==pygame.K_RIGHT:
                to_x+=3 #to_x=to_x+5
            elif event.key==pygame.K_UP:
                to_y-=3
            elif event.key==pygame.K_DOWN:
                to_y+=3
                
        if event.type==pygame.KEYUP: # 키 떼면
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                to_x=0 #x좌표 이동 그만
            elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                to_y=0 #y좌표 이동 그만
                
    character_x_pos += to_x #실제 x좌표는 이동된 좌표
    character_y_pos += to_y #실제 y좌표는 이동된 좌표
    
    if character_x_pos<0: #가로 경계값 처리
        character_x_pos=0
    elif character_x_pos>screen_width-character_width:
        character_x_pos=screen_width-character_width
    if character_y_pos<0: #세로 경계값 처리
        character_y_pos=0
    elif character_y_pos>screen_height-character_height:
        character_y_pos=screen_height-character_height

    #screen.fill((0,0,0))
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    
    pygame.display.update()

    

pygame.quit()