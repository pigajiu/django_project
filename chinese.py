import chardet
import jieba
import os
import  random
from os import path
import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from matplotlib import pyplot as plt
from PIL import Image


def grey_color_func(word,font_size,position,orientation,random_state=None,**kwargs):
    return "hsl(0,0%%,%d%%)" % random.randint(50,100)

#获取当前文件路径
d=path.dirname(__file__) if "__file__" in locals() else os.getcwd()
#获取文本
text=open(path.join(d,'dont cry any more.txt'),'rb').read()
text2=' '.join(jieba.cut(text,cut_all=False))
#设置中文字体
font_path='C:\Windows\Fonts\simkai.ttf'
#读取背景图片
background_Image=np.array(Image.open(path.join(d,"miwa.png")))
#提取背景颜色
img_colors=ImageColorGenerator(background_Image)
#设置中文停止词
stopwords=set('')
stopwords.update(['星星','今天','其实','分享','歌曲','信息','有时候','一样','一直','觉得','www','bbb','亲亲','怎么','真的','还是','这首','flop','哈哈','科学','网易','pv','当年','一些','因为','就是','直到','相比','不要','爱心','为啥','大笑''亲亲','时候','这里','为什么','匹配','没有','竟然','那么','哈哈哈','剧中','评论','我要','好看','憨笑','日子','一次'])

wc=WordCloud(
    font_path=font_path,#中文需要设置路径
    margin = 2,#设置页面边缘
    mask=background_Image,
    scale=2,
    max_words=200,#最多词个数
    min_font_size=4,#最小字体大小
    stopwords=stopwords,
    random_state=30,
    background_color='white',#背景颜色
    max_font_size=80,#最大字体大小
)
#生成词云
wc.generate(text2)
wc.recolor(color_func=img_colors)
#获取文本词排序，可调整stopwords
#process_word=WordCloud.process_text(wc,text2)
#sort=sorted(process_word.items(),key=lambda e:e[1],reverse=True)
#print(sort[:50])
wc.to_file('中文词云.png')
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
plt.show()