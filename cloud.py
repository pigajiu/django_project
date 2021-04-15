import os
from os import path
import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from matplotlib import pyplot as plt
from PIL import Image
import random

#获取当年文件路径
d=path.dirname(__file__) if "__file__" in locals() else os.getcwd()
#获取文本text
text=open(path.join(d,'juben.txt')).read()
#读取背景图片
background_Image=np.array(Image.open(path.join(d,"background.jpg")))
#提取背景颜色
img_colors=ImageColorGenerator(background_Image)
stopwords=set(STOPWORDS)
stopwords.add('Father')
#生成词云
wc = WordCloud(
    margin=2,
    scale=2,
    mask = background_Image,
    max_font_size=150,
    max_words=200,
    min_font_size=4,
    stopwords=stopwords,
    random_state=42,
    background_color='white',

               )
wc.generate_from_text(text)
wc.recolor(color_func=img_colors)
wc.to_file('juben3.png')
#显示图像
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
#存储图像
plt.show()
