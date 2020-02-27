import mecab_parser
from wordcloud import WordCloud


text = "ワードクラウドに含めたいのは名詞とか動詞ですよね。助詞、助動詞が含まれるのはあんまり望ましくない。かと言って、wordcloudの除外キーワード作るの大変そう。と思っていたら"

parsed_text = mecab_parser.mecab(text)
parsed = " ".join(parsed_text)


wordc = WordCloud(font_path="/usr/share/fonts/truetype/fonts-japanese-gothic.ttf",background_color='white',width=800, height=600).generate(parsed)
wordc.to_file('wordcloud.png')
