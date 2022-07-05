import pygame as pg
import sys
import random

def main():
    clock = pg.time.Clock()
    
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600,900))
    screen_rct = screen_sfc.get_rect()
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")
    bgimg_rct = bgimg_sfc.get_rect()
    bgimg_sfc.blit(bgimg_sfc,bgimg_rct)

    koukaton_sfc = pg.image.load("fig/9.png")
    koukaton_sfc = pg.transform.rotozoom(koukaton_sfc,0,2.0)
    koukaton_rct = koukaton_sfc.get_rect()
    koukaton_rct.center = 900,400

    bomb_sfc = pg.Surface((20,20))
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc,(255,0,0),(10,10),10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0,screen_rct.width)   #スクリーンから出ない範囲でランダム
    bomb_rct.centery = random.randint(0,screen_rct.height)

    

    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)
        

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP] == True:    
            koukaton_rct.centery -= 1      #y ... -1
        if key_states[pg.K_DOWN] == True:
            koukaton_rct.centery += 1      #y ... +1
        if key_states[pg.K_LEFT] == True:
            koukaton_rct.centerx -= 1      #x ... -1
        if key_states[pg.K_RIGHT] == True: 
            koukaton_rct.centerx += 1      #x ... +1

        screen_sfc.blit(koukaton_sfc,koukaton_rct)

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()