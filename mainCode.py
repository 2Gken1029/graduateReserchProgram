#! python3
# mainCode.py - 主に使うやつ

# Mecabがどこにあるか調べるコマンド
# $ echo `mecab-config --dicdir`"/mecab-ipadic-neologd"

import MeCab, sys, os, collections
import matplotlib as mpl
mpl.rcParams['font.family'] = 'Hiragino Sans' # 日本語を含むフォントを指定
from matplotlib import pyplot as plt

mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd') # -d以下はechoで調べたパス

if len(sys.argv) < 2:
    print("引数に文章ファイルが指定されていません.")
    print("$ python3 mecabForGraduate.py [文章ファイル]")
    sys.exit()

string_file = open(sys.argv[1])
string_list = string_file.readlines()
string_file.close

# リスト内文字列の"\n"を削除
string_list = [s.replace('\n', '') for s in string_list]

mecab.parse('')#文字列がGCされるのを防ぐ

word_list = []
for string in string_list:
    node = mecab.parseToNode(string)
    while node:
        word = node.surface # 単語を取得
        pos = node.feature.split(",")[1] # 品詞を取得

        #print(word + " : " + pos)
        if(pos=="一般" or pos=="固有名詞" or pos=="サ変接続"): # 特定の名詞のみのリスト
            if not(word=="、" or word=="。" or word=="・" or word=="〜" or word=="○" or word=="?"):
                word_list.append(word)
        #次の単語に進める
        node = node.next

# リスト内の空白要素を削除
wordlist = [s for s in word_list if s != '']

#同じ単語の出現回数を調べる
count_result = collections.Counter(wordlist) # 辞書型を返す
for k, v in count_result.items():
    if  v > 10: # 頻度回数調整
            plt.barh(k,v) # 縦軸に変更する時は、"plt.bar(k,v)"
            #print(k)
#plt.xticks(rotation=90) # X軸ラベルの向きを調整
plt.show()
