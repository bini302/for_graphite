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

background=pygame.image.load("C:/Users/bini3/Desktop/pygame_basic/background.png")
#이벤트 루프
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill((0,0,0))
    #screen.blit(background,(0,0))
    pygame.display.update()

    

pygame.quit()