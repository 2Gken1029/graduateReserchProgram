#! python3
# wordChecker.py - csvファイルからグラフを作成

import csv
import glob
from collections import Counter
import pprint,sys
import matplotlib as mpl
mpl.rcParams['font.family'] = 'Hiragino Sans' # 日本語を含むフォントを指定
from matplotlib import pyplot as plt

# if len(sys.argv) < 2:
#     print("引数に文章ファイルが指定されていません.")
#     print("$ python3 wordChecker.py [文章ファイル]")
#     sys.exit()

csv_list = glob.glob('../Desktop/KHCoder_result/other/*.csv')

rowlist = []

for csv_file in csv_list:
    with open(csv_file) as f:
        reader = csv.reader(f)
        for row in reader:
            rowlist.append(row)

noun_list = []
verb_list = []
adjective_list = []
adverb_list = []
other_list = []

for list in rowlist:
    if list[1] == '名詞' or list[1] == 'サ変名詞':
       noun_list.append(list[0])
    elif list[1] == '動詞':
        verb_list.append(list[0])
    elif list[1] == '形容詞':
        adjective_list.append(list[0])
    elif list[1] == '副詞可能':
        adverb_list.append(list[0])
    else:
        other_list.append(list[0])

count_result = Counter(adverb_list)
percent = 0.0

for k,v in count_result.items():
    if v > len(csv_list) * 0.2:
        percent = v / len(csv_list)
        plt.barh(k,percent)

plt.show()