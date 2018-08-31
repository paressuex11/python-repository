import wordcloud
import jieba
f=open("xdd.txt","r+",encoding="utf-8")
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=" ".join(ls)
w=wordcloud.WordCloud(width=4000,height=4000,font_path='msyh',max_words=30)
w.generate(txt)
w.to_file("xdd.png")
