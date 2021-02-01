#! python3
# wordChecker.py - csvファイルからグラフを作成

import csv
import glob
from collections import Counter
import pprint,sys
import matplotlib as mpl
mpl.rcParams['font.family'] = 'Hiragino Sans' # 日本語を含むフォントを指定
from matplotlib import pyplot as plt

csv_list = glob.glob('../Documents/graduateReserchData/KHCoder_result/cutListResult/結/*.csv')

rowlist = []

for csv_file in csv_list:
    with open(csv_file) as f:
        reader = csv.reader(f)
        for row in reader:
            rowlist.append(row)

wordlist = []

for list in rowlist:
    if not list[1] == '品詞':
        if not list[1] == '感動詞':
            wordlist.append(list[0])

count_result = Counter(wordlist)

percent = 0.0

for k,v in count_result.items():
    if v > len(csv_list) * 0.3: # 割合調整
        percent = v / len(csv_list)
        # print(k + " ," + str(percent)) # CSV出力用
        if percent > 1.0: percent = 1.0 # 100%以上のとき100%で打ち止め
        plt.barh(k,percent)

plt.show()