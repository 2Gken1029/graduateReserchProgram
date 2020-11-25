#! python3
# countCode.py - 引数で指定したテキストファイルの単語数を調べる

import sys, os

if len(sys.argv) < 2:
    print("引数に文章ファイルが指定されていません.")
    print("$ python3 mecabForGraduate.py [文章ファイル]")
    sys.exit()

string_file = open(sys.argv[1])
string_list = string_file.readlines()
string_file.close

# リスト内文字列の特定文字を削除
string_list = [s.replace('\n', '') for s in string_list]
string_list = [s.replace('、', '') for s in string_list]
string_list = [s.replace('。', '') for s in string_list]
string_list = [s.replace('？', '') for s in string_list]
# リスト内文字列を全て結合
word_all = ''.join(string_list)

print(len(word_all))