import pygame as pg
import sys

def main():
    clock = pg.time.Clock()
    
    pg.display.set_caption("逃げろ")
    screen = pg.display.set_mode((1600,900))

    clock.tick(0.5)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exist()