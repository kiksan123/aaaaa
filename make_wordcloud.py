import mecab_parser
from wordcloud import WordCloud


with open("sample.txt","r") as f:
    text = f.read()
parsed_text = mecab_parser.mecab(text)
parsed = " ".join(parsed_text)

print(parsed)

wordc = WordCloud(font_path="/usr/share/fonts/truetype/fonts-japanese-gothic.ttf",background_color='white',width=800, height=600).generate(parsed)
wordc.to_file('wordcloud.png')
