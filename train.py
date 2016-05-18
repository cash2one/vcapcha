# coding=utf-8


import time
import requests
import os
from pcha import ecp
from PIL import Image
from pytesseract import image_to_string

path = '/scqcp'
home = '/home/august/vcapcha/png' + path
if not os.path.exists(home):
    os.mkdir(home)
os.chdir(home)

url = 'http://scqcp.com/rCode.jpg'

def cnoise(fn):
    if fn.endswith('.png'):
        im = Image.open(fn)
        im = im.convert('L')
        im = im.point(lambda x: 255 if x > 160 else 0)
        im = ecp(im)
        return im
        # nfn = fn[:-4] + '_g.png'
        # print(nfn)
        # im.save(nfn)

def getImage(url, i):
    print('Downloading {0} <== {1}'.format(i, url))
    r = requests.get(url)
    fn = '00' + str(i) + '.png'
    with open(fn, 'wb') as f:
        f.writelines(r.content)
    return fn

def vcode(fn):
    im = cnoise(fn)
    code = image_to_string(im, lang='scqcp', config='-psm 8')
    new = code + '.png'
    os.rename(fn, new)
    return code

for x in xrange(100, 200):
    fn = getImage(url, x)
    print fn
    print(vcode(fn))
    time.sleep(0.75)







# for x in os.listdir(home):
#     cnoise(x)

# 生成box
# cmd = 'sh genBox.sh '.format(home, )

# for x in os.listdir(home):
#     if x.endswith('g.png'):
#         cmd = 'convert {0} -flatten -monochrome {1}.tif'.format(x, x[:-4])
#         os.system(cmd)
# cmd = 'tiffcp -c none *.tif target.tif'
# os.system(cmd)
# os.system('mv target.tif code.font.exp0.tif')
# os.system(cmd)
# cmd = 'tesseract -psm 8 code.font.exp0.tif code.font.exp0 batch.nochop makebox'
# os.system(cmd)
# cmd = 'tesseract -psm 8 code.font.exp0.tif code.font.exp0 box.train'
# os.system(cmd)

# 生成data
# cmd = './genData.sh {0} {1}'.format('png' + path, home.split('/')[-1])
# print(cmd)
# os.system(cmd)
