#! python3
# mecabSampleCode.py - Mecabの基本的な使い方を改変

# Mecabがどこにあるか調べるコマンド
# $ echo `mecab-config --dicdir`"/mecab-ipadic-neologd"

import MeCab,os,sys

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
        #単語を取得
        word = node.surface
        word_list.append(word)
        #次の単語に進める
        node = node.next

# リスト内の空白要素を削除
wordlist = [s for s in word_list if s != '']
# リスト内の特定の単語を削除
wordList = [s for s in wordlist if s != 'Transcript']

print(wordList)
print(len(wordList))