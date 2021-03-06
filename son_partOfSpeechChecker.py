#! python3
# partOfSpeechChecker.py - 指定したCSVファイルの特定の品詞を一つのリストにまとめる

import summarize
from collections import Counter
import glob
import sys
import matplotlib as mpl
mpl.rcParams['font.family'] = 'Hiragino Sans' # 日本語を含むフォントを指定
from matplotlib import pyplot as plt

if len(sys.argv) < 2:
    print("引数に文章ファイルが指定されていません.")
    print("$ python3 partOfSpeechChecker.py [数字]もしくは[品詞]")
    print("名詞: 1 or noun\n動詞: 2 or verb\n形容詞: 3 or adjective\n副詞: 4 or adverb")
    sys.exit()

option_name = sys.argv[1]

csv_list = glob.glob('csvfile/son_csvfile/*.csv')
noun_list = []

# 全CSVファイルの特定の品詞を結合
if(option_name == "1" or option_name == "noun"):
    plt.title("son_名詞")
    for csv_name in csv_list:
        noun_list.extend(summarize.noun(csv_name))
elif(option_name == "2" or option_name == "verb"):
    plt.title("son_動詞")
    for csv_name in csv_list:
        noun_list.extend(summarize.verb(csv_name))
elif(option_name == "3" or option_name == "adjective"):
    plt.title("son_形容詞")
    for csv_name in csv_list:
        noun_list.extend(summarize.adjective(csv_name))
elif(option_name == "4" or option_name == "adverb"):
    plt.title("son_副詞")
    for csv_name in csv_list:
        noun_list.extend(summarize.adverb(csv_name))
else:
    print("指定したオプションは存在しません:")
    print("名詞: 1 or noun\n動詞: 2 or verb\n形容詞: 3 or adjective\n副詞: 4 or adverb")
    sys.exit()

#同じ単語の出現回数を調べる, グラフ軸を縦軸に変更する時は、"plt.bar(k,v)"
count_result = Counter(noun_list) # 辞書型を返す
percent = 0.0
if(option_name == "1" or option_name == "noun" or
    option_name == "2" or option_name == "verb"):
    for k, v in count_result.items():
        if v > len(csv_list) * 0.4:
            percent = v / len(csv_list)
            plt.barh(k,percent)
else:
    for k, v in count_result.items():
        percent = v / len(csv_list)
        plt.barh(k,percent)
#plt.xticks(rotation=90) # X軸ラベルの向きを調整
plt.show()