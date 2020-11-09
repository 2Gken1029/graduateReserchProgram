# -*- coding: utf-8 -*-
#! python3
# summarizeNoun.py - csvファイルから得た単語リストの共通値を調べる

import csv
import pandas as pd
import numpy as np
import pprint

# 名詞
def noun(filename):
    csvfile = pd.read_csv(str(filename),header=0)
    noun_list = []

    # 名詞の全ヘッダー名
    header_name_noun = ['名詞', 'サ変名詞', '形容動詞', '固有名詞', '組織名', 
                        '人名', '地名', 'ナイ形容', '副詞可能', '未知語', '感動詞']

    header_list = list(csvfile) # 読み込んだcsvファイルのヘッダーリスト

    for header_name in header_name_noun:
        if header_name in header_list:
            first_list = list(csvfile[header_name])
            for s in first_list:
                # nan以外の値をリストに格納
                if isinstance(s,str) or np.isfinite(s):
                    noun_list.append(s)

    noun_list = set(noun_list) # 重複してる単語を削除
    return noun_list

# 動詞
def verb(filename):
    csvfile = pd.read_csv(str(filename),header=0)
    verb_list = []
    header_list = list(csvfile) # 読み込んだcsvファイルのヘッダーリスト

    if "動詞" in header_list: # 形容詞が存在するか
        first_list = list(csvfile['動詞'])
        for s in first_list:
            # nan以外の値をリストに格納
            if isinstance(s,str) or np.isfinite(s):
                verb_list.append(s)

    return verb_list

# 形容詞
def adjective(filename):
    csvfile = pd.read_csv(str(filename),header=0)
    adjective_list = []
    header_list = list(csvfile) # 読み込んだcsvファイルのヘッダーリスト

    if "形容詞" in header_list: # 形容詞が存在するか
        first_list = list(csvfile['形容詞'])
        for s in first_list:
            # nan以外の値をリストに格納
            if isinstance(s,str) or np.isfinite(s):
                adjective_list.append(s)

    return adjective_list

# 副詞
def adverb(filename):
    csvfile = pd.read_csv(str(filename),header=0)
    adverb_list = []
    header_list = list(csvfile) # 読み込んだcsvファイルのヘッダーリスト

    if "副詞" in header_list: # 形容詞が存在するか
        first_list = list(csvfile['副詞'])
        for s in first_list:
            # nan以外の値をリストに格納
            if isinstance(s,str) or np.isfinite(s):
                adverb_list.append(s)

    return adverb_list