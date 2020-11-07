#! python3
# partOfSpeechChecker.py - 指定したCSVファイルの特定の品詞を一つのリストにまとめる

import summarize
from collections import Counter
import glob
import sys

if len(sys.argv) < 2:
    print("引数に文章ファイルが指定されていません.")
    print("$ python3 partOfSpeechChecker.py [数字]もしくは[品詞]")
    print("名詞: 1 or noun\n動詞: 2 or verb\n形容詞: 3 or adjective\n副詞: 4 or adverb")
    sys.exit()

option_name = sys.argv[1]

csv_list = glob.glob('csvfile/*.csv')
noun_list = []

# 全CSVファイルの特定の品詞を結合
if(option_name == "1" or option_name == "noun"):
    for csv_name in csv_list:
        noun_list.extend(summarize.noun(csv_name))
elif(option_name == "2" or option_name == "verb"):
    for csv_name in csv_list:
        noun_list.extend(summarize.verb(csv_name))
elif(option_name == "3" or option_name == "adjective"):
    for csv_name in csv_list:
        noun_list.extend(summarize.adjective(csv_name))
elif(option_name == "4" or option_name == "adverb"):
    for csv_name in csv_list:
        noun_list.extend(summarize.adverb(csv_name))
else:
    print("指定したオプションは存在しません:")
    print("名詞: 1 or noun\n動詞: 2 or verb\n形容詞: 3 or adjective\n副詞: 4 or adverb")
    sys.exit()

print(Counter(noun_list))