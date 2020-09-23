#! python3
# percentage.py - wordFind.pyで調べた結果より危険率を考察

import os, sys
import wordFind

if len(sys.argv) < 2:
    print("引数に音声文章ファイルが指定されていません.")
    print("$ python3 wordFind.py [音声文章ファイル]")
    sys.exit()

apper_word = wordFind.wordFind(sys.argv[1])
print(apper_word)