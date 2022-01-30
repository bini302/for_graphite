#pip install pygame 터미널에서 파이게임 설치
import pygame #잘 설치됐는지 확인

pygame.init() #필수(초기화)

#화면크기
screen_width=480 #가로
screen_height=640 #세로
screen=pygame.display.set_mode((screen_width,screen_height)) #화면크기 설정

#화면 타이틀
pygame.display.set_caption("for graphite") #게임 이름
#다음 명령이 없으면 창은 자동으로 꺼짐

# fps
clock = pygame.time.Clock()

#배경불러오기
background=pygame.image.load("C:/Users/bini3/Desktop/pygame_basic/background.png")

#캐릭터 불러오기
character=pygame.image.load("C:/Users/bini3/Desktop/pygame_basic/character.png")
character_size=character.get_rect().size #rect로 캐릭터 크기 구해옴
character_width=character_size[0] #character_size 문자열의 첫번째 값(가로)
character_height=character_size[1] #character_size 문자열의 두번째 값(세로)
character_x_pos=screen_width/2-character_width/2
character_y_pos=screen_height-character_height

#이동할 좌표
to_x=0
to_y=0

#이동속도
character_speed=0.6

#적캐릭터
enemy=pygame.image.load("C:/Users/bini3/Desktop/pygame_basic/enemy.png")
enemy_size=enemy.get_rect().size
enemy_width=enemy_size[0]
enemy_height=enemy_size[1]
enemy_x_pos=screen_width/2-enemy_width/2
enemy_y_pos=screen_height/2-enemy_height/2

#폰트 정의
game_font=pygame.font.Font(None, 40) #폰트 객체 생성, (폰트(기본값), 크기)

#총 시간
total_time=10

#시작 시간
start_ticks=pygame.time.get_ticks() #현재 tick 받아옴
#시간계산은 처음에 tick을 받아와서 현재 tick을 받아오는 방식


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

    #충돌 처리를 위한 rect 정보 업데이트
    #rect에 좌표, width, height 다 들어있음
    #character는 이동해서 출력되지만 실제 이미지 좌표는 처음 설정한 그대로임
    character_rect=character.get_rect()
    character_rect.left=character_x_pos
    character_rect.top=character_y_pos
        
    enemy_rect=enemy.get_rect()
    enemy_rect.left=enemy_x_pos
    enemy_rect.top=enemy_y_pos
    #위에서 한건 변수설정, 그리기라서 이제 적이랑 캐릭터가 실제로 존재함
    
    #충돌 체크
    if character_rect.colliderect(enemy_rect):
    #colliderect(x): x와 충돌했는지 확인하는 함수
        print("충돌")
        running=False
        

    #screen.fill((0,0,0))
    screen.blit(background,(0,0)) #배경그리기
    screen.blit(character,(character_x_pos,character_y_pos)) #캐릭터 그리기
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos)) #적 그리기
    
    
    #타이머
    #경과 시간 계산
    elapsed_time=(pygame.time.get_ticks()-start_ticks)/1000
    #경과된 시간=(현재 시간-시작 시간)/1000
    #경과 시간을(ms) 1000으로 나눠서 초(s) 단위 표시
    timer=game_font.render(str(int(total_time-elapsed_time)), True, (255,255,255))
    #초 단위만 보여주기위해 int, render에 문자가 들어오도록 str
    #출력값, true(무조건이라는데??), 글자색(rgb)
    screen.blit(timer, (10,10)) #위치
    if total_time-elapsed_time<=0:
        print("타임아웃")
        running=False
    
    pygame.display.update() #게임 화면 업데이트

#종료 전 잠시 대기
pygame.time.delay(2000) #2초 대기(ms)

pygame.quit()