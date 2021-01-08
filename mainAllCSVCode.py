#! python3
# wordChecker.py - csvファイルからグラフを作成

import csv
import glob
from collections import Counter
import pprint,sys
import matplotlib as mpl
mpl.rcParams['font.family'] = 'Hiragino Sans' # 日本語を含むフォントを指定
from matplotlib import pyplot as plt

if len(sys.argv) == 2 and int(sys.argv[1]) < 6:
    part_of_speech = int(sys.argv[1])
else:
    print('エラー発生')
    sys.exit()
 
csv_list = glob.glob('../Documents/graduateReserchData/KHCoder_result/allCSV/*.csv')

print(len(csv_list))

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
        if not list[1] == '品詞':
            other_list.append(list[0])

if part_of_speech == 1:
    count_result = Counter(noun_list)
elif part_of_speech == 2:
    count_result = Counter(verb_list)
elif part_of_speech == 3:
    count_result = Counter(adjective_list)
elif part_of_speech == 4:
    count_result = Counter(adverb_list)
elif part_of_speech == 5:
    count_result = Counter(other_list)

percent = 0.0

for k,v in count_result.items():
    if v > len(csv_list) * 0.0: # 割合調整
        percent = v / len(csv_list)
        if percent > 1.0: percent = 1.0 # 100%以上のとき100%で打ち止め
        plt.barh(k,percent)

plt.show()