# -*- coding: utf-8 -*-

# Programı resimlerin oldugu mevcut diziye atın ve sonra çalıştırın.
# Not : 'pip install Pillow'  şeklinde modülü kurmanız lazım.

import os
from PIL import Image

mevcut_dizin = os.getcwd()
liste1 = os.listdir(mevcut_dizin)

liste2 = []
liste3 = []

extensions = ("png", "bmp", "gif", "png", "tifjpg", "jp2", "j2k", "jpeg")
for i in range(len(liste1)):
    if any([liste1[i].endswith(x) for x in extensions]):
        liste2.append(Image.open(mevcut_dizin + "\\" + liste1[i]))

print(liste1)

for k in range(len(liste2)):
    liste3.append(liste2[k].convert('RGB'))

liste3[0].save(mevcut_dizin + "\\" + "pdfAdı.pdf", save_all=True, append_images=liste3[1::])
