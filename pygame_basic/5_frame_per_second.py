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

# fps
clock = pygame.time.Clock()

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
#이동속도
character_speed=0.6

#이벤트 루프
running=True
while running:
    dt=clock.tick(60) #게임 화면의 초당 프레임 수 설정, 'x'프레임
    
    #그냥 이렇게 설정하면 프레임 수에 따라 캐릭터 속도가 달라짐.
    #ex) fps(10) : 초당 10회 작동, 100만큼 움직이려면 1회에 10만큼 이동
    #    fps(20) : 초당 20회 작동, 100만큼 움직이려면 1회에 5만큼 이동
    #       =>기존 코드는 단순히 1회에 얼마나 움직일지 설정해놔서 이제 fps에 따라 속도가 안바뀌도록
    #         추가 설정을 해야함. 키가 눌렸을때 character_speed만큼 움직임.
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN: #키가 눌렸다면
            if event.key==pygame.K_LEFT:
                to_x-=character_speed #fps때문에 바꿈
            elif event.key==pygame.K_RIGHT:
                to_x+=character_speed
            elif event.key==pygame.K_UP:
                to_y-=character_speed
            elif event.key==pygame.K_DOWN:
                to_y+=character_speed
                
        if event.type==pygame.KEYUP: # 키 떼면
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                to_x=0 #x좌표 이동 그만
            elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                to_y=0 #y좌표 이동 그만
                
    character_x_pos += to_x*dt #dt(fps)만 곱해주면 됨
    character_y_pos += to_y*dt 
    
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