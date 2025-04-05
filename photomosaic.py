from PIL import Image, ImageDraw, ImageFont
import os

def divide(im, big, small):
    ret = []
    for i in range(int(big[0] / small[0])):
        for j in range(int(big[1] / small[1])):
            tup = (i * small[0], j * small[1], (i + 1) * small[0], (j + 1) * small[1])
            ret.append(im.crop(tup))
    return ret

def average(im, dim):
    ans = [0, 0, 0]
    for i in range(dim[0]):
        for j in range(dim[1]):
            temp = im.getpixel((i, j))
            ans[0] += temp[0]
            ans[1] += temp[1]
            ans[2] += temp[2]
    t = dim[0] * dim[1]
    ans[0] = int(ans[0] / t)
    ans[1] = int(ans[1] / t)
    ans[2] = int(ans[2] / t)
    return ans

def colour(img):
    ans = "#"
    temp = hex(img[0])[2:]
    if len(temp) == 1:
        temp = "0" + temp
    ans += temp
    temp = hex(img[1])[2:]
    if len(temp) == 1:
        temp = "0" + temp
    ans += temp
    temp = hex(img[2])[2:]
    if len(temp) == 1:
        temp = "0" + temp
    ans += temp
    return ans.upper()

def pixelate(im, big, small, ret):
    img = im.copy()
    draw = ImageDraw.Draw(img)
    k = 0
    for i in range(int(big[0] / small[0])):
        for j in range(int(big[1] / small[1])):
            tup = [(i * small[0], j * small[1]), ((i + 1) * small[0], (j + 1) * small[1])]
            draw.rectangle(tup, outline = "Black", fill = colour(ret[k]), width = 0)
            k += 1
    return img

def format(filename):
    file = open(filename, "r")
    ans = []
    for line in file:
        if len(line) == 0:
            return im
        line = line.strip().split()
        ans.append(line)
    return ans

def nearest(tup, lst, dirPath):
    min = -1
    ind = -1
    for t in lst:
        a = (tup[0] - int(t[0])) ** 2 + (tup[1] - int(t[1])) ** 2 + (tup[2] - int(t[2])) ** 2
        if a < min or min == -1:
            min = a
            ind = lst.index(t)
    directory = dirPath
    k = 0
    ans = ""
    for filename in os.listdir(directory):
        if k == ind:
            ans = "mosaic\\" + filename
        k += 1
    img = Image.open(ans)
    return img


def photomosaic(im, avg, big, small, lst, dirPath):
    k = 0
    for i in range(int(big[0] / small[0])):
        for j in range(int(big[1] / small[1])):
            tup = [i * small[0], j * small[1], (i + 1) * small[0], (j + 1) * small[1]]
            img = nearest(avg[k], lst, dirPath).resize(small)
            img.convert("RGBA")
            img.convert("RGB")
            im.paste(img, tup)
            k += 1
    return im


im = Image.open("image.jpg")
im = im.resize((4096, 4096))
imgSize = [4096, 4096]
secSize = [128, 128]

ans = divide(im, imgSize, secSize)

avg = []

for img in ans:
    avg.append(average(img, secSize))

lst = format("averageColours.txt")
pm = im.copy()
dirPath = "C:\\Users\\Puskar\\Desktop\\photomosaic\\mosaic"
pm = photomosaic(pm, avg, imgSize, secSize, lst, dirPath)
pm.show()
im.show()
