import wordcloud
import jieba
f=open('xdd.txt',encoding='utf-8')
t=f.read()
f.close()
ls=jieba.lcut(t)
ls=" ".join(ls)
w=wordcloud.WordCloud(width=2000,height=2000,font_path='msyh')
w.generate(ls)
w.to_file('xdd.png')
