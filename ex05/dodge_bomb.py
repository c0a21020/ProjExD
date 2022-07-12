import selectors
import pygame as pg
import sys
import random


class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]: 
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]: 
            self.rct.centery += 1
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]: 
            self.rct.centerx += 1

        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]: 
                self.rct.centery += 1
            if key_states[pg.K_DOWN]: 
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]: 
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]: 
                self.rct.centerx -= 1
        self.blit(scr)

    def attack(self):       #メインでスペースキーが押されると、この処理が行われる
        return Beam(self)


class Bomb:
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate   
        self.blit(scr)   


class Beam:                          #（追加クラス）スペースキーが押されると、こうかとんからビームが出る
    def __init__(self, chr: Bird):
        self.sfc = pg.image.load("fig/beam.png")
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 0.2)
        self.rct = self.sfc.get_rect()
        self.rct.midleft = chr.rct.center

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        self.rct.move_ip(+10, 0)
        self.blit(scr)
        if check_bound(self.rct, scr.rct) != (1, 1):
            del self    


class bgm:                                 #（追加クラス）ゲームが始まるとBGMが流れる
    def __init__(self, music):
        pg.mixer.init(frequency = 44100)
        pg.mixer.music.load(music)
        pg.mixer.music.play(1)


def main():
    clock = pg.time.Clock()
    scr = Screen("負けるな！こうかとん", (1430, 765), "fig/pg_bg.jpg")
    kkt = Bird("fig/8.png", 2.0, (900, 400))
    bkd1 = Bomb((255, 0, 0), 10, (+1, +1), scr)
    bkd2 = Bomb((255, 255, 0), 14, (+3, -1), scr)   #爆弾追加
    bkd3 = Bomb((0, 128, 0), 8, (-1, +2), scr)   #爆弾追加
    bkd4 = Bomb((0, 0, 128), 11, (+1, +1), scr)   #爆弾追加
    bgm("fig/Tchaikovsky-Symphony-No5-2nd-2020-AR.mp3") #チャイコフスキーしかダウンロードできませんでした汗
                                                        #チャイコフスキーがBGMで流れます汗
    flag = 0  #フラグは基本０だが、スペースキーが押されるとき、flag=1になり、Beamクラスが動く
    
    while True:
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:  #スペースキーが押されるとビームが出る
                flag = 1
                beam = kkt.attack()

        kkt.update(scr)
        bkd1.update(scr)
        bkd2.update(scr)
        bkd3.update(scr)
        bkd4.update(scr)
        if flag == 1:
            beam.update(scr)
        #４つの爆弾がこうかとんにぶつかったとき
        if kkt.rct.colliderect(bkd1.rct):
            return
        if kkt.rct.colliderect(bkd2.rct):
            return
        if kkt.rct.colliderect(bkd3.rct):
            return
        if kkt.rct.colliderect(bkd4.rct):
            return

        pg.display.update()
        clock.tick(1000)

def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right :
        yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: 
        tate = -1 # 領域外
    return yoko, tate


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
