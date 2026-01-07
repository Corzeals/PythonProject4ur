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
'''
class alarm:
'''

def stop_ur(screen, startticks):
    font = pygame.freetype.SysFont(None, 100)
    font.origin = True

    ticks = pygame.time.get_ticks()- startticks
    millis = ticks % 1000
    seconds = int(ticks / 1000 % 60)
    minutes = int(ticks / 60000 % 24)
    out = '{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
    font.render_to(screen, (270, 100), out, pygame.Color(GREEN))
    pygame.display.flip()
if __name__ == '__stopur__': stopur()


def main():
    font = pygame.freetype.SysFont(None, 100)
    font.origin = True

    run = True
    vis_stopur = False
    ticks = 0

    click_areal = pygame.Rect(0,20,250,100)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                if click_areal.collidepoint(pygame.mouse.get_pos()):
                    print('good')
                    if vis_stopur:
                        vis_stopur = False
                    else:
                        vis_stopur = True
                        ticks = pygame.time.get_ticks()
                    print(pygame.mouse.get_pos())



        now=datetime.datetime.now()

        current_time_str = now.strftime("%H:%M:%S")

        screen.fill(BLACK)
        pygame.draw.rect(screen, (200, 1, 5), pygame.Rect(0, 20, 250, 100))
        font.render_to(screen, (0,100), 'start:', pygame.Color(GREEN))
        ur(current_time_str,200,WHITE,(WIDTH/2,HEIGHT/2))
        if vis_stopur:
            stop_ur(screen,ticks)

        pygame.display.flip()

        pygame_ur.tick(FPS)
    pygame.quit()
if __name__ == "__main__":
    main()