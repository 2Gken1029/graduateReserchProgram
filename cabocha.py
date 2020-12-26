import CaboCha
import sys

c = CaboCha.Parser()

if len(sys.argv) < 2:
    print("引数に文章ファイルが指定されていません.")
    print("$ python3 mecabForGraduate.py [文章ファイル]")
    sys.exit()

with open(sys.argv[1]) as f:
    s = f.read()

sentence = s

tree =  c.parse(sentence)

# 形態素を結合しつつ[{c:文節, to:係り先id}]の形に変換する
chunks = []
text = ""
toChunkId = -1
for i in range(0, tree.size()):
    token = tree.token(i)
    text = token.surface if token.chunk else (text + token.surface) 
    toChunkId = token.chunk.link if token.chunk else toChunkId
    # 文末かchunk内の最後の要素のタイミングで出力
    if i == tree.size() - 1 or tree.token(i+1).chunk:
       chunks.append({'c': text, 'to': toChunkId})

# 係り元→係り先の形式で出力する
for chunk in chunks:
    if chunk['to'] >= 0:
        print(chunk['c'] + " →　" + chunks[chunk['to']]['c'])
