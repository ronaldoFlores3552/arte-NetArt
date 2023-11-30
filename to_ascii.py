
from PIL import Image, ImageOps
import numpy as np
import cv2
from matplotlib import pyplot as plt

CONST_DICE_VALS = [1, 2, 3, 4, 5, 6]
CONST_ASCII_TEST = ['.', ':', '|', 'U', '$', '@']


def define_steps(val):
    return 256 // val


def calc_range(pix_val, step):
    incr = step
    count = 0
    while pix_val > incr:
        count += 1
        incr += step
        if incr > 255:
            count = 5
            break
    return count


def write_result(res, step):
    f = open("resultFile.txt", "w+")
    for row in res:
        for col in row:
            val = calc_range(col, step)
            # dice_val = CONST_DICE_VALS[val]
            dice_val = CONST_ASCII_TEST[val]
            f.write(str(dice_val) + ' ')
        f.write("\n")
    f.close()


def convert_to_grayscale(img_path):
    im = Image.open(img_path)
    value = ImageOps.grayscale(im)
    value.save('static/gray_img.jpg')
    img = cv2.imread("static/gray_img.jpg")
    res = cv2.resize(img, dsize=(75, 100), interpolation=cv2.INTER_CUBIC)
    single_byte_res = [[col[0] for col in row] for row in res]
    step = define_steps(6)
    write_result(single_byte_res, step)
    #plt.imshow(single_byte_res, interpolation='nearest')
    plt.imsave('static/result.png', single_byte_res, cmap='gray')

