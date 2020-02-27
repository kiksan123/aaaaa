import MeCab as mc

CONTENT_WORD = set(["形容詞", "動詞","名詞", "形容動詞"])

def mecab(text):
    tt = mc.Tagger("-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/")
    tt.parse('')
    node = tt.parseToNode(text) 
    output = []
    while node:
        if node.surface != "":  # ヘッダとフッタを除外
            word_type = node.feature.split(",")[0]
            if word_type in CONTENT_WORD:
                output.append(node.surface)
        node = node.next
        if node is None:
            break
    return output

# sample
print(mecab("今日のエヴァンゲリオン出動予定は中止です"))

