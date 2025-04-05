import os
from PIL import Image, ImageDraw, ImageFont

def average(im, dim):
    ans = [0, 0, 0]
    for i in range(dim[0]):
        for j in range(dim[1]):
            im = im.convert("RGBA")
            im = im.convert("RGB")
            temp = im.getpixel((i, j))
            ans[0] += temp[0]
            ans[1] += temp[1]
            ans[2] += temp[2]
    t = dim[0] * dim[1]
    ans[0] = int(ans[0] / t)
    ans[1] = int(ans[1] / t)
    ans[2] = int(ans[2] / t)
    return ans

directory = "C:\\Users\\Puskar\\Desktop\\photomosaic\\mosaic"

file = open("averageColours.txt", "w")

"""for line in file:
    print(line.strip())"""

for filename in os.listdir(directory):
    img = Image.open("mosaic\\" + filename)
    img = img.resize((64, 64))
    tup = average(img, [64, 64])
    file.write(str(tup[0]) + " " + str(tup[1]) + " " + str(tup[2]) + "\n")

file.close()
    