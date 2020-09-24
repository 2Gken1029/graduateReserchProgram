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
        pos = node.feature.split(",")[1] # 品詞を取得
        if(pos == "一般"):
            word_list.append(word)
        #次の単語に進める
        node = node.next

# リスト内の空白要素を削除
wordlist_1 = [s for s in word_list if s != '']
# リスト内の特定の単語を削除
wordlist_2 = [s for s in wordlist_1 if s != 'Waiting'] # 音声文字起こしの初期システム通知
wordlist_3 = [s for s in wordlist_2 if s != 'for']
wordlist_4 = [s for s in wordlist_3 if s != 'operation']
wordlist_5 = [s for s in wordlist_4 if s != 'to']
wordlist_6 = [s for s in wordlist_5 if s != 'complete']
wordlist_7 = [s for s in wordlist_6 if s != 'Transcript']
wordlist = [s for s in wordlist_7 if s != ':']

print(wordlist)
print(len(wordlist))