import pygame

pygame.init()
screenw,screenh=500,500

screen=pygame.display.set_mode((screenw,screenh))
pygame.display.set_caption("my first bg")

img=pygame.transform.scale(pygame.image.load('C:/Users/Mira Rana/OneDrive/Pictures/Screenshots/confused_screaming.png').convert(),(300,300))
img_rect=img.get_rect(center=(screenw//2,screenh//2-30))
def game_loop():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        screen.blit(img,img_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__ == '__main__':
    game_loop()