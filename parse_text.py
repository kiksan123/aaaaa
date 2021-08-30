import pandas
import mecab_parser

def parse_textfile(filename):
    """textファイルからtextを読み込んでリスト化する
    Args:
        filename(str):ファイル名
    Returns:
        text_L(list):1テキストずつ入ったリスト

    """

    with open(filename,"r") as f:
        text_L = f.readlines()
    
    print(text_L)
    return text_L

    

if __name__=="__main__":
    parse_textfile("./sampledata/test_corpus.txt")