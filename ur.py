import pygame
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
'''class alarm:

class stopur:

class timer:'''


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

        pygame.display.flip()

        ur.tick(FPS)
    pygame.quit()
if __name__ == "__main__":
    main()