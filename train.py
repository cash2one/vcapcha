# coding=utf-8


import time
import requests
import os
import re
from pcha import ecp, fff, top
from PIL import Image, ImageEnhance, ImageFilter
import cv2
from pytesseract import image_to_string
from fabric.colors import green

path = '/jslw'
home = '/home/august/vcapcha/png' + path
if not os.path.exists(home):
    os.mkdir(home)
os.chdir(home)

# url = 'http://www.e2go.com.cn/Home/LoginCheckCode/'
# url = 'http://www.bus365.com/imagevalidate/createValidateImage'
url = 'http://www.jslw.gov.cn/verifyCode'


def cnoise(fn):
    if fn.endswith('.png'):
        im = Image.open(fn)
        im = im.convert('L')
        im = im.point(lambda x: 255 if x > 180 else 0)

        # im = cv2.imread(fn)
        # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        # im = cv2.adaptiveThreshold(
        #     im, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 40)

        im = ecp(im, 8)
        im = fff(im, 4, 30)
        # im = im.filter(ImageFilter.MedianFilter())
        # im.show()
        # return im

        nfn = fn[:-4] + '_g.png'
        print(nfn)
        # cv2.imwrite(nfn, im)
        im.save(nfn)


def getImage(url, i=None):
    print('Downloading {0} <== {1}'.format(i, url))
    r = requests.get(url)
    fn = '00' + str(i) + '.png'
    with open(fn, 'wb') as f:
        f.writelines(r.content)
    return fn


def printColor(fn):
    im = Image.open(fn)
    top(im)


def vcode(fn):
    im = cnoise(fn)
    try:
        # lang = 'e2go1'
        # cmd = 'tesseract {0} 1 -l {1} -psm 8'.format(fn, lang)
        # os.system(cmd)
        code = image_to_string(im, lang='e2go', config='-psm 8')
        # print(code)
        info = re.findall(r'[0-9a-zA-Z]', str(code))
        code = ''.join(info)
        if len(code.strip()) != 4:
            return 'Failed!!!'
        new = code + '.png'
        os.rename(fn, new)
        return code
    except Exception as e:
        print(e)


def start(n, init=0):
    for x in xrange(init, n):
        fn = getImage(url, x)
        print fn
        try:
            cnoise(fn)
        except Exception as e:
            print(e)
        # print(vcode(fn))
        time.sleep(0.5)

start(100)


def lstart(home):
    for x in os.listdir(home):
        if '_' not in x:
            cnoise(x)
            # printColor(x)
            print(green(2333))

# lstart(home)

def rmNonSource(home):
    for x in os.listdir(home):
        if '_' in x:
            os.remove(x)
# rmNonSource(home)


# 生成box
# cmd = 'sh genBox.sh '.format(home, )

for x in os.listdir(home):
    if x.endswith('g.png'):
        cmd = 'convert {0} -flatten -monochrome {1}.tif'.format(x, x[:-4])
        os.system(cmd)
cmd = 'tiffcp -c none *.tif target.tif'
os.system(cmd)
os.system('mv target.tif code.font.exp0.tif')
cmd = 'tesseract -psm 8 code.font.exp0.tif code.font.exp0 batch.nochop makebox'
os.system(cmd)

# 生成data
# 解压 combine_tessdata -u eng.traineddata eng/eng.
cmd = './genData.sh {0} {1}'.format('png' + path, home.split('/')[-1])
print(cmd)
# os.system(cmd)
