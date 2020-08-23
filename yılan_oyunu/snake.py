import pygame
import sys
import random

class Hedef():
    def __init__(self):
        self.konum = (0,0)
        self.renk = (223, 163, 49)
        self.rasgele_konumlandır()

    def rasgele_konumlandır(self):
        self.konum = (random.randint(0, kare_genisligi-1)*kareboyutu, random.randint(0, kare_uzunlugu-1)*kareboyutu)

    def draw(self, yüzey):
        r = pygame.Rect((self.konum[0], self.konum[1]), (kareboyutu, kareboyutu))
        pygame.draw.rect(yüzey, self.renk, r)
        pygame.draw.rect(yüzey, (0, 0, 0), r, 1)

def zemin_ciz(yüzey):
    for y in range(0, int(kare_uzunlugu)):
        for x in range(0, int(kare_genisligi)):
            if (x+y)%2 == 0:
                r = pygame.Rect((x*kareboyutu, y*kareboyutu), (kareboyutu,kareboyutu))
                pygame.draw.rect(yüzey,(3,91,22), r)
            else:
                rr = pygame.Rect((x*kareboyutu, y*kareboyutu), (kareboyutu,kareboyutu))
                pygame.draw.rect(yüzey, (3,91,22), rr)

class Yılan():
    def __init__(self):

        self.renk = (255, 10, 10)

        self.puan = 0

        self.uznluk = 1

        self.konum = [((ekran_yüksekligi/2), (ekran_genişliği/2))]

        self.kontrol = random.choice([yukarı, asagı, sol, sag])

    def reset(self):
        self.uznluk = 1
        self.konum = [((ekran_yüksekligi / 2), (ekran_genişliği / 2))]
        self.kontrol = random.choice([yukarı, asagı, sol, sag])
        self.puan = 0

    def kafa_konumunu_don(self):
        return self.konum[0]


    def hareket(self):
        kafa = self.kafa_konumunu_don()
        x,y = self.kontrol
        ek = (((kafa[0]+(x*kareboyutu))%ekran_yüksekligi), (kafa[1]+(y*kareboyutu))%ekran_genişliği)
        if len(self.konum) > 2 and ek in self.konum[2:]:
            self.reset()
        else:
            self.konum.insert(0,ek)
            if len(self.konum) > self.uznluk:
                self.konum.pop()

    def don(self, point):
        if self.uznluk > 1 and (point[0]*-1, point[1]*-1) == self.kontrol:
            return
        else:
            self.kontrol = point


    def draw(self,yüzey):
        for p in self.konum:
            r = pygame.Rect((p[0], p[1]), (kareboyutu,kareboyutu))
            pygame.draw.rect(yüzey, self.renk, r)
            pygame.draw.rect(yüzey, (0,0, 0), r, 1)

    def tus_kontrol(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.don(yukarı)
                elif event.key == pygame.K_DOWN:
                    self.don(asagı)
                elif event.key == pygame.K_LEFT:
                    self.don(sol)
                elif event.key == pygame.K_RIGHT:
                    self.don(sag)



ekran_yüksekligi = 800
ekran_genişliği = 600

kareboyutu = 20
kare_genisligi = ekran_yüksekligi / kareboyutu
kare_uzunlugu = ekran_genişliği / kareboyutu

yukarı = (0,-1)
asagı = (0,1)
sol = (-1,0)
sag = (1,0)

def main():
    pygame.init()

    zmn = pygame.time.Clock()
    ekran = pygame.display.set_mode((ekran_yüksekligi, ekran_genişliği), 0, 32)

    yüzey = pygame.Surface(ekran.get_size())
    yüzey = yüzey.convert()
    zemin_ciz(yüzey)

    yılan = Yılan()
    yemek = Hedef()

    font = pygame.font.SysFont("verdana bold",36)

    while (True):
        zmn.tick(14)

        yılan.tus_kontrol()

        zemin_ciz(yüzey)

        yılan.hareket()

        if yılan.kafa_konumunu_don() == yemek.konum:
            yılan.uznluk += 1
            yılan.puan += 1
            yemek.rasgele_konumlandır()


        yılan.draw(yüzey)
        yemek.draw(yüzey)


        ekran.blit(yüzey, (0,0))
        text = font.render("puan {0}".format(yılan.puan), 1, (0,0,0))

        ekran.blit(text, (5,10))
        pygame.display.update()

main()
