#! python3
# percentage.py - wordFind.pyで調べた結果より危険率を考察

import os, sys
import wordFind

if len(sys.argv) < 2:
    print("引数に音声文章ファイルが指定されていません.")
    print("$ python3 wordFind.py [音声文章ファイル]")
    sys.exit()

apper_word = wordFind.wordFind(sys.argv[1]) # 引数よりwordFind.pyを使用
print(apper_word)

apper_word_len = len(apper_word)
print("出現した単語は " + str(apper_word_len) + "個")

apper_word_value = 0 # 初期化
for k,v in apper_word.items(): # 各valueの値を総合
    print("[" + k + "]" + "が出現した回数: " + str(v))
    apper_word_value = v + apper_word_value

print("keyとvalueの総合値: " + str(apper_word_len+apper_word_value))