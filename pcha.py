# coding=utf-8

from operator import itemgetter


def rmbg(im, cp=20, r=0):
    w, h = im.size
    for x in xrange(w):
        for y in xrange(h):
            pix = im.getpixel((x, y))
            if pix < (cp, cp, cp):
                im.putpixel((x, y), (255, 255, 255))
    return im


def top(im):
    im = im.convert('P')
    his = im.histogram()
    values = {}
    for i in range(256):
        values[i] = his[i]
    # 排名前十的色彩, pix依据这里值进行判断
    for j, k in sorted(values.items(), key=itemgetter(1), reverse=True)[:10]:
        print j, k


def ecp(im, dcount=6):
    frame = im.load()
    (w, h) = im.size
    for i in xrange(w):
        for j in xrange(h):
            if frame[i, j] != 255:
                count = 0
                try:
                    if frame[i, j - 1] == 255:
                        count += 1
                except IndexError:
                    pass
                try:
                    if frame[i, j + 1] == 255:
                        count += 1
                except IndexError:
                    pass
                try:
                    if frame[i - 1, j - 1] == 255:
                        count += 1
                except IndexError:
                    pass
                try:
                    if frame[i - 1, j] == 255:
                        count += 1
                except IndexError:
                    pass
                try:
                    if frame[i - 1, j + 1] == 255:
                        count += 1
                except IndexError:
                    pass
                try:
                    if frame[i + 1, j - 1] == 255:
                        count += 1
                except IndexError:
                    pass
                try:
                    if frame[i + 1, j] == 255:
                        count += 1
                except IndexError:
                    pass
                try:
                    if frame[i + 1, j + 1] == 255:
                        count += 1
                except IndexError:
                    pass
                if count >= dcount:
                    frame[i, j] = 255
    return im


def fff(im, way=4, mincount=8):
    frame = im.load()
    (w, h) = im.size
    points = []
    processedpoints = []
    global goodpoints
    goodpoints = []
    for x in xrange(w):
        for y in xrange(h):
            color = frame[x, y]
            if color == 255 or ((x, y) in processedpoints):
                continue
            processedpoints.append((x, y))

            points.append((x, y))

            # points.remove((x,y))
            for (x, y) in points:

                try:
                    if frame[x, y - 1] == color and (x, y - 1) not in points:
                        points.append((x, y - 1))
                except:
                    pass
                try:
                    if frame[x, y + 1] == color and (x, y + 1) not in points:
                        points.append((x, y + 1))
                except:
                    pass
                try:
                    if frame[x - 1, y] == color and (x - 1, y) not in points:
                        points.append((x - 1, y))
                except:
                    pass
                try:
                    if frame[x + 1, y] == color and (x + 1, y) not in points:
                        points.append((x + 1, y))
                except:
                    pass
                if way == 8:
                    try:
                        if frame[x - 1, y - 1] == color and (x - 1, y - 1) not in points:
                            points.append((x - 1, y - 1))
                    except:
                        pass
                    try:
                        if frame[x + 1, y - 1] == color and (x + 1, y - 1) not in points:
                            points.append((x + 1, y - 1))
                    except:
                        pass
                    try:
                        if frame[x - 1, y + 1] == color and (x - 1, y + 1) not in points:
                            points.append((x - 1, y + 1))
                    except:
                        pass
                    try:
                        if frame[x + 1, y + 1] == color and (x + 1, y + 1) not in points:
                            points.append((x + 1, y + 1))
                    except:
                        pass
            processedpoints.extend(points)
            # print color,len(points)
            # print points
            if 1 < len(points) < mincount:
                for (x, y) in points:
                    # print x,y
                    frame[x, y] = 255
            if len(points) > 16:
                goodpoints.extend(points)

            points = []

    return im
