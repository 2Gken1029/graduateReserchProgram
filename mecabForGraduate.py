#! python3
# mecabForGraduate.py - mecabSampleCodeを改変

# Mecabがどこにあるか調べるコマンド
# $ echo `mecab-config --dicdir`"/mecab-ipadic-neologd"

import MeCab, sys, os

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

for string in string_list:
    node = mecab.parseToNode(string)
    while node:
        #単語を取得
        word = node.surface
        print(word)
        #次の単語に進める
        node = node.next