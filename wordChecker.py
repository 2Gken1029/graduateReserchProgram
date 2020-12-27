#! python3
# wordChecker.py - csvファイルからグラフを作成

import csv
import glob
from collections import Counter
import pprint,sys
import matplotlib as mpl
mpl.rcParams['font.family'] = 'Hiragino Sans' # 日本語を含むフォントを指定
from matplotlib import pyplot as plt

if len(sys.argv) == 3:
    path = sys.argv[1]
    if int(sys.argv[2]) < 5:
        part_of_speech = int(sys.argv[2])
    else:
        sys.exit()
else:
    path = 'son'
    part_of_speech = 1

csv_list = glob.glob('../Documents/graduateReserchData/KHCoder_result/'+str(path)+'/*.csv')

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
    if v > len(csv_list) * 0.4:
        percent = v / len(csv_list)
        plt.barh(k,percent)

if path == 'son':
    plt.title('オレオレ詐欺(息子)')
elif path == 'police':
    plt.title('オレオレ詐欺(警察官)')
elif path == 'other':
    plt.title('還付金詐欺')

plt.show()