import pygame
pygame.init()

win=pygame.display.set_mode((1100,500))
pygame.display.set_caption("Rectangle Moving")

x=100
y=100
width=40
height=60
vel=10

run=True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel-10:
        x-=vel
    if keys[pygame.K_RIGHT] and x < 1100-width-vel+10:
        x+=vel
    if keys[pygame.K_UP] and y > vel-10:
        y-=vel
    if keys[pygame.K_DOWN] and y < 500-height-vel+10:
        y+=vel
    if keys[pygame.K_LALT] and keys[pygame.K_F4]:
        run=False

    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x,y,width,height))
    pygame.display.update()
        



pygame.quit()
