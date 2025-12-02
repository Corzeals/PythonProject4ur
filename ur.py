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
ur=pygame.time.Clock()



class digitalt_ur:
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
class stopur:
    def stop_ur(screen):
        font = pygame.freetype.SysFont(None, 100)
        font.origin = True

        ticks = pygame.time.get_ticks()
        millis = ticks % 1000
        seconds = int(ticks / 1000 % 60)
        minutes = int(ticks / 60000 % 24)
        out = '{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
        font.render_to(screen, (100, 100), out, pygame.Color(GREEN))
        pygame.display.flip()
if __name__ == '__stopur__': stopur()

'''
class timer:
'''

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        now=datetime.datetime.now()

        current_time_str = now.strftime("%H:%M:%S")

        screen.fill(BLACK)

        digitalt_ur.ur(current_time_str,200,WHITE,(WIDTH/2,HEIGHT/2))
        stopur.stop_ur(screen)

        pygame.display.flip()

        ur.tick(FPS)
    pygame.quit()
if __name__ == "__main__":
    main()