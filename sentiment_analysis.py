# Imports the Google Cloud client library
from google.cloud import language_v1
from google.cloud import language_v1beta2


def sentence_predict(sentence_L):

    # Instantiates a client
    #client = language_v1.LanguageServiceClient()
    client = language_v1beta2.LanguageServiceClient()

    language = "ja"
    # The text to analyze
    for text in sentence_L:

        #document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT,language=language)
        document = language_v1beta2.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT,language=language)

        # Detects the sentiment of the text
        sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

        print("Text: {}".format(text))
        print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))

if __name__=="__main__":
    L = ["今日は牛丼をいっぱい食べて満足。幸福感がすごい",
         "今日は雨で野球の試合が中止。とても悲しい。"]
    sentence_predict(L)
    