import pygame as pg
import sys

def main():
    clock = pg.time.Clock()
    

    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600,900))
    screen_rct = screen_sfc.get_rect()
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")
    bgimg_rct = bgimg_sfc.get.rect()
    bgimg_sfc.blit(bgimg_sfc,bgimg_rct)
    
    pg.display.update()

    clock.tick(0.2)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exist()