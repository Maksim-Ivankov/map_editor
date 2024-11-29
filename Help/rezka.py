from PIL import Image

# Разрезка чанков на 4 части

import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import os

count_img = os.listdir('src/img/map_grid/Tile_rename')

for i in count_img:
    print(i)
    im = Image.open(f'src/img/map_grid/Tile_rename/{i}')
    x0 = 0
    y0 = 0
    x1 = 480
    y1 = 480
    im_crop = im.crop((x0, y0, x1, y1))
    number = f'src/img/map_grid/Tile_png_chetwert/{i[:-4]}.png' 
    im_crop.save(number, quality=100)
    im = Image.open(f'src/img/map_grid/Tile_rename/{i}')
    x0 = 480
    y0 = 0
    x1 = 960
    y1 = 480
    im_crop = im.crop((x0, y0, x1, y1))
    number = f'src/img/map_grid/Tile_png_chetwert/{i[:-4]}.25.png' 
    im_crop.save(number, quality=100)
    im = Image.open(f'src/img/map_grid/Tile_rename/{i}')
    x0 = 0
    y0 = 480
    x1 = 480
    y1 = 960
    im_crop = im.crop((x0, y0, x1, y1))
    number = f'src/img/map_grid/Tile_png_chetwert/{i[:-4]}.5.png' 
    im_crop.save(number, quality=100)
    im = Image.open(f'src/img/map_grid/Tile_rename/{i}')
    x0 = 480
    y0 = 480
    x1 = 960
    y1 = 960
    im_crop = im.crop((x0, y0, x1, y1))
    number = f'src/img/map_grid/Tile_png_chetwert/{i[:-4]}.75.png' 
    im_crop.save(number, quality=100)

# im = Image.open(self.path_img_celka)
# x0 = (j)*TILESIZE*COUNT_CHANK
# y0 = (i-1)*TILESIZE*COUNT_CHANK
# x1 = (j)*TILESIZE*COUNT_CHANK + TILESIZE*COUNT_CHANK
# y1 = (i-1)*TILESIZE*COUNT_CHANK + TILESIZE*COUNT_CHANK
# im_crop = im.crop((x0, y0, x1, y1))
# number = (int(self.number_img_celka)-1)*9 + (i-1)*3 + (j+1)
# im_crop.save(f'src/img/map_grid/Tile_png/{number}.png', quality=100)