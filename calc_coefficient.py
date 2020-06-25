import numpy as np
import MeCab
from sklearn.feature_extraction.text import CountVectorizer
import mecab_parser
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

def morphological_analysis(sentence_L,label_L):
    """形態素解析を行いone-hot-vector(Bag of words)にして返す
    Args:
        sentence_L(list):文のリスト eg:) ["こんにちは世界","今日の天気は晴れ"]
        label_L(list):文のラベル　eg:) [1,0]
    Returns:
        bow(np.array):one-hot-vector
        label_L(list):label
        words_L(list):one-hot-vectorに対応するwords

    """
    result_L = []

    for f in sentence_L:
        r = mecab_parser.mecab(f)
        r = " ".join(r)
        result_L.append(r)

    docs = np.array(result_L)
    count = CountVectorizer()
    bags = count.fit_transform(docs)
    bow = bags.toarray()
    features = count.get_feature_names()
    words_L = features

    return bow,label_L,words_L

def calc_coef(bow,label_L,words_L):


    lr = LogisticRegression()
    lr.fit(bow, label_L)
    coef = lr.coef_

    for i in range(len(words_L)):
        print(words_L[i],coef[0][i])

    print("切片",lr.intercept_)
    
    pred = lr.predict(bow)
    print("debug_acc",accuracy_score(label_L,pred))
    print("debug_precision",precision_score(label_L,pred))
    print("debug_recall",recall_score(label_L,pred))
    print("debug_f1_score",f1_score(label_L,pred))


if __name__=="__main__":
    #this is sample code
    ## create demo data
    sentence_L = ["本日は良い天気ですね",
                  "本日の天気を教えてください",
                  "ホワイトボードと僕は仲良しです",
                  "チョコと飴とコップと時計",
                  "明日と本日の天気は同じです",
                  "ホワイトボードと僕は似ています"]
    labels = [0,0,1,1,0,1]

    # calc coef
    bow,label_L,words_L = morphological_analysis(sentence_L,labels)
    calc_coef(bow,labels,words_L)
