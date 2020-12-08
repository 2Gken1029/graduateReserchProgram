#! python3
# -*- coding: utf-8 -*-

# このコードで困ったらよしくんに聞く
# imageJoin.py - 画像を結合させる

from PIL import Image
import glob
import os
from pprint import pprint

path = "imageFolder"
targetPath = "resultFolder"

files = os.listdir(path)
# files_list = [f for f in files if os.path.isfile(os.path.join(path, f))]
files_list = glob.glob(os.path.join(path, '*.png'))
sorted_list = sorted(files_list, key=lambda f: os.stat(f).st_mtime, reverse=True)

# im1 = Image.open("./imageFolder/" + files_list[0])
# im2 = Image.open("./imageFolder/" + files_list[1])

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

for index in range(0, len(sorted_list), 2):
    im2 = Image.open(sorted_list[index])
    im1 = Image.open(sorted_list[index+1])
    result_name = str(index//2) + '-' + sorted_list[index].split('/')[1].split('.')[0] + '.png'
    get_concat_v(im1, im2).save(os.path.join(targetPath, result_name))
