import pygame as pg
import sys
import random

def main():
    clock = pg.time.Clock()
    
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1430,765))
    screen_rct = screen_sfc.get_rect()
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")
    bgimg_rct = bgimg_sfc.get_rect()
    bgimg_sfc.blit(bgimg_sfc,bgimg_rct)

    koukaton_sfc = pg.image.load("fig/9.png")
    koukaton_sfc = pg.transform.rotozoom(koukaton_sfc,0,2.0)
    koukaton_rct = koukaton_sfc.get_rect()
    koukaton_rct.center = 900,400

    x,y = 20,20
    #bomb1
    bomb_sfc = pg.Surface((x,y))
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc,(255,0,0),(10,10),x-10)
    pg.draw.circle(bomb_sfc,(191,0,0),(10,10),x-12)
    pg.draw.circle(bomb_sfc,(127,0,0),(10,10),x-14)
    pg.draw.circle(bomb_sfc,(63,0,0),(10,10),x-16)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0,screen_rct.width)   #スクリーンから出ない範囲でランダム
    bomb_rct.centery = random.randint(0,screen_rct.height)

    #bomb2
    bomb2_sfc = pg.Surface((x,y))
    bomb2_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb2_sfc,(255,0,0),(10,10),x-10)
    pg.draw.circle(bomb2_sfc,(191,0,0),(10,10),x-12)
    pg.draw.circle(bomb2_sfc,(127,0,0),(10,10),x-14)
    pg.draw.circle(bomb2_sfc,(63,0,0),(10,10),x-16)
    bomb2_rct = bomb2_sfc.get_rect()
    bomb2_rct.centerx = random.randint(0,screen_rct.width)   #スクリーンから出ない範囲でランダム
    bomb2_rct.centery = random.randint(0,screen_rct.height)

    #bomb3
    bomb3_sfc = pg.Surface((x,y))
    bomb3_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb3_sfc,(255,0,0),(10,10),x-10)
    pg.draw.circle(bomb3_sfc,(191,0,0),(10,10),x-12)
    pg.draw.circle(bomb3_sfc,(127,0,0),(10,10),x-14)
    pg.draw.circle(bomb3_sfc,(63,0,0),(10,10),x-16)
    bomb3_rct = bomb3_sfc.get_rect()
    bomb3_rct.centerx = random.randint(0,screen_rct.width)   #スクリーンから出ない範囲でランダム
    bomb3_rct.centery = random.randint(0,screen_rct.height)

    #bomb1,2,3 がそれぞれのスピード、向きで動くように変化量を変更
    vx, vy = +1, +1
    vx2, vy2 = -0.8, +1.3
    vx3, vy3 = +1.4, -1.1
    

    

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

        if check_bound(koukaton_rct,screen_rct) != (1,1):
            if key_states[pg.K_UP] == True:
                koukaton_rct.centery += 1      #y ... -1
            if key_states[pg.K_DOWN] == True:
                koukaton_rct.centery -= 1      #y ... +1
            if key_states[pg.K_LEFT] == True:
                koukaton_rct.centerx += 1      #x ... -1
            if key_states[pg.K_RIGHT] == True: 
                koukaton_rct.centerx -= 1      #x ... +1
        screen_sfc.blit(koukaton_sfc,koukaton_rct)
        
        #pg.init()が呼ばれてからの経過時間をpasstimeとし、
        #passtimeが0.1秒ずつ増加する時の処理
        passtime = pg.time.get_ticks()
        if passtime % 100 == 0:
            vx,vy,vx2,vy2,vx3,vy3 = +2, +2, -2, +2, +2, -2     #３つの爆弾の増加量を０.1秒ずつ増やすことで、徐々に速度を速くしている
            bomb_sfc = pg.transform.rotozoom(bomb_sfc,0,1.2)   #３つの爆弾の比率を1.2倍にすることで、0.1秒ずつ爆弾が大きくなる
            bomb2_sfc = pg.transform.rotozoom(bomb2_sfc,0,1.2)
            bomb3_sfc = pg.transform.rotozoom(bomb3_sfc,0,1.2)
        
        bomb_rct.move_ip(vx,vy)
        bomb2_rct.move_ip(vx2,vy2)
        bomb3_rct.move_ip(vx3,vy3)
        
        screen_sfc.blit(bomb_sfc,bomb_rct)
        screen_sfc.blit(bomb2_sfc,bomb2_rct)
        screen_sfc.blit(bomb3_sfc,bomb3_rct)
        
        yoko,tate = check_bound(bomb_rct,screen_rct)
        vx *= yoko
        vy *= tate

        yoko,tate = check_bound(bomb2_rct,screen_rct)
        vx2 *= yoko
        vy2 *= tate

        yoko,tate = check_bound(bomb3_rct,screen_rct)
        vx3 *= yoko
        vy3 *= tate

        
        if koukaton_rct.colliderect(bomb_rct):
            print("爆弾がこうかとんに当たってしまった...")
            return
        if koukaton_rct.colliderect(bomb2_rct):
            print("爆弾がこうかとんに当たってしまった...")
            return
        if koukaton_rct.colliderect(bomb3_rct):
            print("爆弾がこうかとんに当たってしまった...")
            return

        pg.display.update()
        clock.tick(1000)

def check_bound(rct, scr_rct):
    
    '''
    [1] rct: こうかとんor爆弾 の　Rect
    [2] scr_rct: スクリーンのRect
    '''
    yoko,tate = +1,+1
    if rct.left < scr_rct.left or scr_rct.right < rct.right:
        yoko = -1
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom:
        tate = -1
    return yoko,tate

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()