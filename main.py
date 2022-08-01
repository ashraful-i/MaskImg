# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PIL import Image
from os import listdir
from os.path import isfile, join
import pandas as pd

def read2():
    mypath = "D:\ibtd\ibtd\Mask"
    maskImages = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    R_skin = [0 for x in range(256)]
    G_skin = [0 for x in range(256)]
    B_skin = [0 for x in range(256)]
    Skin_RGB = [[[0 for x in range(256)] for y in range(256)] for z in range(256)]
    total_skin = 0
    for maskimg in maskImages:
        # print(maskimg)
        im = Image.open(mypath + "\\" + maskimg)
        pix = im.load()
        im_w = im.size[0]
        im_h = im.size[1]
        # print(im_h, im_w)

        for x in range(im_w):
            for y in range(im_h):
                Blue = pix[x, y][2]
                Green = pix[x, y][1]
                Red = pix[x, y][0]
                Skin_RGB[Red][Blue][Green] += 1
                if Red == 255 and Blue == 255 and Green == 255:
                    continue
                else:
                    R_skin[Red] += 1
                    G_skin[Green] += 1
                    B_skin[Blue] += 1
                    total_skin += 1
    print(R_skin)
    non_skin = "D:\ibtd\ibtd\Test"
    non_skin_Images = [f for f in listdir(non_skin) if isfile(join(non_skin, f))]
    Non_Skin_RGB = [[[0 for x in range(256)] for y in range(256)] for z in range(256)]
    total_non_skin = 0
    R_nskin = [0 for x in range(256)]
    G_nskin = [0 for x in range(256)]
    B_nskin = [0 for x in range(256)]
    for non_s in non_skin_Images:
        # print(maskimg)
        im = Image.open(non_skin + "\\" + non_s)
        pix = im.load()
        im_w = im.size[0]
        im_h = im.size[1]
        # print(im_h, im_w)

        for x in range(im_w):
            for y in range(im_h):
                Blue = pix[x, y][2]
                Green = pix[x, y][1]
                Red = pix[x, y][0]
                Non_Skin_RGB[Red][Blue][Green] += 1

                R_nskin[Red] += 1
                G_nskin[Green] += 1
                B_nskin[Blue] += 1
                total_non_skin += 1
    print(R_nskin)

    im = Image.open("man.jpg")
    pix = im.load()
    im_w = im.size[0]
    im_h = im.size[1]
    # print(im_h, im_w)
    print("check")
    for x in range(im_w):
        for y in range(im_h):
            Red = pix[x, y][0]
            Green = pix[x, y][1]
            Blue = pix[x, y][2]
            probab = ((R_skin[Red] * G_skin[Green] * B_skin[Blue]) / (total_skin * total_skin * total_skin)) / (
                    (R_nskin[Red] * G_nskin[Green] * B_nskin[Blue]) / (total_non_skin * total_non_skin * total_non_skin))
            if (probab > 1):
                pix[x, y] = (0, 0, 0)
    im.save("probab.jpg")
    im.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read2()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
