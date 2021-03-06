#! python3
# wordFind.py - 単語リストにある単語が文章ファイルにどれほどでてくるか

import os, sys

def wordFind(file_name):
    word_file = open('frequentList.txt') # 単語リストを読み込み
    word_list = word_file.readlines() # リストに書き込み
    word_file.close()

    voice_file = open(file_name) # 最初の引数を音声文章ファイルとする
    voice_list = voice_file.readlines()
    voice_file.close

    # リスト内文字列の"\n"を削除
    word_list = [s.replace('\n', '') for s in word_list]
    voice_list = [s.replace('\n', '') for s in voice_list]

    # 音声文章の中に特定の単語が含まれているか
    appear_word = {}
    for voice in voice_list:
        for word in word_list:
            if word in voice: # 有無
                ### print("・" + word + "  " + voice) ###
                if not word in appear_word: # 初めて特定の単語が含まれていたら記録
                    appear_word[word] = 1
                else: # 再び単語が含まれていたらカウントを1増やす
                    appear_word[word] = appear_word[word] + 1

    return appear_word