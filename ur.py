import pygame
import pygame.freetype
import datetime

WIDTH = 800
HEIGHT = 800
FPS = 60
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("digitalt ur")
pygame_ur=pygame.time.Clock()




def ur(number,size,color,position):

    try:
        font = pygame.font.SysFont("Arial", size, True ,False)
    except:
        font = pygame.font.Font(None, size)
    text = font.render(number, True, color)
    textRect = text.get_rect(center=position)
    screen.blit(text,textRect)

def stop_ur(screen, startticks):
    font = pygame.freetype.SysFont(None, 100)
    font.origin = True

    ticks = pygame.time.get_ticks()- startticks
    millis = ticks % 1000
    seconds = int(ticks / 1000 % 60)
    minutes = int(ticks / 60000 % 24)
    out = '{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
    font.render_to(screen, (270, 100), out, pygame.Color(GREEN))

if __name__ == '__stopur__': stop_ur()

def timer(screen, endticks):
    font_2 = pygame.freetype.SysFont(None, 100)
    font_2.origin = True

    ticks = endticks-pygame.time.get_ticks()
    seconds = int(ticks / 1000 % 60)
    minutes = int(ticks / 60000 % 24)

    out_timer = '{minutes:02d}:{seconds:02d}'.format(minutes=minutes, seconds=seconds)
    font_2.render_to(screen, (300, 200), out_timer, pygame.Color(GREEN))


if __name__ == '__timer__': timer()

def main():
    font = pygame.freetype.SysFont(None, 100)
    font.origin = True

    run = True
    vis_stopur = False
    sekundtimer = False
    ticks = 0
    værdi = 0
    endticks = -1
    click_areal = pygame.Rect(0,20,250,100)
    click_areal_2 = pygame.Rect(0,100 , 250, 100)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and sekundtimer:
                if chr(event.key).isdigit():
                    char = chr(event.key)
                    værdi = værdi * 10 + int(char)
                    print(værdi)
                else:
                    sekundtimer = False
                    endticks = pygame.time.get_ticks() + værdi * 1000
            if event.type == pygame.MOUSEBUTTONDOWN:


                if click_areal.collidepoint(pygame.mouse.get_pos()):
                    if vis_stopur:
                        vis_stopur = False
                    else:
                        vis_stopur = True
                        ticks = pygame.time.get_ticks()
                    print(pygame.mouse.get_pos())

                if click_areal_2.collidepoint(pygame.mouse.get_pos()):

                    sekundtimer = True
                    print('colide')
                    print(værdi)



        now=datetime.datetime.now()

        current_time_str = now.strftime("%H:%M:%S")

        screen.fill(BLACK)

        if endticks > pygame.time.get_ticks():
            timer(screen, endticks)
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 20, 250, 100))
            værdi = 0
        else:
            font.render_to(screen,(0, 700), 'tast sekunder:', pygame.Color(GREEN))
        if vis_stopur:
            font.render_to(screen, (0,100), 'stop:', pygame.Color(GREEN))
        else:
            font.render_to(screen, (0, 100), 'start:', pygame.Color(GREEN))

        ur(current_time_str,200,WHITE,(WIDTH/2,HEIGHT/2))
        if vis_stopur:
            stop_ur(screen,ticks)
        font.render_to(screen, (0, 200), 'timer:', pygame.Color(GREEN))



        pygame.display.flip()

        pygame_ur.tick(FPS)
    pygame.quit()
if __name__ == "__main__":
    main()