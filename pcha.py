# coding=utf-8


def ecp(im):
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
                if count >= 6:
                    frame[i, j] = 255
    return im
