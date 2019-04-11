# NLTK 学习笔记
## 前记
相关链接深入阅读

- [https://www.nltk.org](https://www.nltk.org)	
- [https://docs.python.org/3/](https://docs.python.org/3/)

书籍勘误信息
- [http://www.oreilly.com/catalog/9780596516499](http://www.oreilly.com/catalog/9780596516499)
## 1 语言处理及Python
### 1.1 语言计算:文本及词汇
#### NLTK入门
```python
# 导入及浏览下载软件包
import nltk
nltk.download()
```
```python
from nltk.book import *
"""
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
"""
```
```
文本1:《白鲸记》-赫尔曼·梅尔维尔,1851年
文本2:《感觉与情感》-简·奥斯汀,1811年
文本3:创世纪之书
文本4:就职演说语料库
文本5:聊天语料库
文本6:巨蟒和圣杯
文本7:华尔街日报
文本8:个人语料库
文本9:《代号星期四》-切斯特顿,1908年
```

#### 搜索文本
```python
# 查找《白鲸记》中的词monstrous
text1.concordance("monstrous")
# 查找出现在相似上下文中的词
text1.similar("monstrous")
# 研究共用两个或两个以上词汇的上下文
text1.common_contexts(["monstrous","very"])

# 画分布图需要引用 numpy 和 matplotlib
# 离散图表示从文本开头算起有多少词出现的位置信息
text4.dispersion_plot(["citizens","democracy","freedom","duties","America"])

# 产生相似风格的随机文本,标点符号和单词分开
text3.generate()
```
#### 计数词汇
```python
# 列表操作(计算长度,排序,去重,追加)
len(text3)
sorted(set(text3))	# 大写字母出现在小写字母之前
len(set(text3))
text3.count("smote")
```
### 1.2 近观Python:将文本当做词链表
```python
text3+text4
sent1.append("Some")
# 索引列表,索引从0开始
text4[173]
text4.index('awaken')
```
### 1.3 计算语言:简单的统计
#### 频率分布
```python
fdist1=FreqDist(text1)
"""
>>> fdist1
FreqDist({',': 18713, 'the': 13721, '.': 6862, 'of': 6536, 'and': 6024, 'a': 456
9, 'to': 4542, ';': 4072, 'in': 3916, 'that': 2982, ...})
"""
fdist1.plot(50,cumulative=True) # 前50个词的积累频率图
vocabulary1=list(fdist1.keys()) # 字典键值变列表
vocabulary1[:50]	# 切片
fdist1.hapaxes()	# 只出现1词的词
```
#### 细粒度的选择词
链表推导条件式
```python
V = set(text1)
long_words = [w for w in V if len(w)>15]

fdist5=FreqDist(text5)
sorted([w for w in set(text5) if len(w)>7 and fdist5[w]>7])
```
#### 词语搭配和双连词
**搭配**是不经常在一起出现的词序列
```python
# 获取词对
bigrams(['more','is','said','than','done','!'])
"""
>>> list(bigrams(['more','is','said','than','done','!']))
[('more', 'is'), ('is', 'said'), ('said', 'than'), ('than', 'done'), ('done', '!')]
"""
# 找到出现频率比预期频率更频繁的双联词
text4.collocations()

```
#### 计算其他东西
除了计算词汇外,还可以计算词长等

> #####  表1-2   NLTK频率分布类中定义的函数

|例子|描述|
|:-|:-|
|fdist = FreqDist(text1)	|创建包含给定样本的分布
|fdist.inc(text1)			|增加样本
|fdist['monstrous'] 		|计数给定样本出现的次数
|fdist.freq('monstrous')	|给定样本的频率
|fdist.N 					|样本总数
|fdisk.keys()				|以频率递减顺序排序的样本链表
|for sample in fdist:		|以频率递减的顺序遍历样本
|fdist.max()				|数值最大的样本
|fdist.tabulate()			|绘制频率分布表
|fdist.plot()				|绘制频率分布图
|fdist.plot(cumulative=True)|绘制积累频率分布图
|fdist1<fdist2				|测试样本在fdist1中出现的频率是否小于fdist2

### 1.4 回到Python:决策与控制

> #####  表1-3 数值比较运算符(略)

> #####  表1-4 词汇比较运算符
|函数|含义|
|:-|:-|
|s.startswith(t)	|测试s是否以t开头
|s.endswith(t)		|测试s是否以t结尾
|t in s				|测试s是否包含t
|s.islower()		|测试s中所有字符是否都是小写字母
|s.isupper()		|测试s中所有字符是否都是大写字母
|s.isalpha()		|测试s中所有字符是否都是字母
|s.isalnum()		|测试s中所有字符是否都是字母或数字
|s.isdigit()		|测试s中所有字符是否都是数字
|s.istitle()		|测试s是否首字母大写(s中的所有词都首字母大写)

#### 对每个元素进行操作
处理
- 链表推导
	- `[f(w) for ...]`
	- `[w.f() for ...]`

- 过滤字母,不区分大小写
	- `set([w.lower() for w in text1 if w.isalpha()])`
#### 嵌套代码块(略)
#### 条件循环(略)
	
### 1.5 自动理解自然语言
#### 词义消歧
要分析出特定上下文中的词被赋予的是哪个意思
#### 指代消解(anaphora resolution):
处理这个问题的计算技术包括:

- 确定代词或名词指的是什么
- 语义角色标注(semantic role labeling):确定名词短语如何与动词相关联(如代理、受事、工具等)
	
#### 自动生成语言

#### 机器翻译

```python
babelize_shell()
```
> **文本对齐**:自动配对组成句子的过程

#### 人机对话系统
```python
nltk.chat.chatbots()
```
#### 文本的含义
文本含义识别(`Recognizing Textual Entailment,RTE`)

## 获得文本语料和词汇资源
### 2.1 获取文本语料库
#### 古腾堡语料库
[http://www.gutenberg.org](http://www.gutenberg.org)
```python
nltk.corpus.gutenberg.fileids()
"""
['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', 'bible-kjv.txt', 'blake-poems.txt', 
'bryant-stories.txt', 'burgess-busterbrown.txt', 'carroll-alice.txt', 'chesterton-ball.txt', 'chesterton-brown.txt', 
'chesterton-thursday.txt', 'edgeworth-parents.txt', 'melville-moby_dick.txt', 'milton-paradise.txt', 
'shakespeare-caesar.txt', 'shakespeare-hamlet.txt', 'shakespeare-macbeth.txt', 'whitman-leaves.txt']
"""

emma =  nltk.corpus.gutenberg.words('austen-emma.txt')
"""['[', 'Emma', 'by', 'Jane', 'Austen', '1816', ']', ...]"""

# 研究nltk.corpus中的数据
emma_text = nltk.Text(emma)
emma_text.concordance("surprize")

```
#### 网络聊天文本
```python
from nltk.corpus import webtext
for fileid in webtext.fileids():
	print(fileid,webtext.raw(fileid)[:30],'...')
"""
firefox.txt Cookie Manager: "Don't allow s ...
grail.txt SCENE 1: [wind] [clop clop clo ...
overheard.txt White guy: So, do you have any ...
pirates.txt PIRATES OF THE CARRIBEAN: DEAD ...
singles.txt 25 SEXY MALE, seeks attrac old ...
wine.txt Lovely delicate, fragrant Rhon ...
"""

from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
chatroom[123]
"""
['i', 'do', "n't", 'want', 'hot', 'pics', 'of', 'a', 'female', ',', 'I', 'can',
'look', 'in', 'a', 'mirror', '.']
"""
"""
即时消息聊天群会话语料库
10-19-20s_706posts.xml表示2006年10月19日从20多岁聊天室收集的706个帖子
"""

```
#### 布朗语料库
布朗大学1961年创建,第一个百万词级的英语电子语料库

文体列表参见[http://icame.uib.no/brown/bcm-los.html](http://icame.uib.no/brown/bcm-los.html)
> 注 访问不了

```python
from nltk.corpus import brown
brown.categories()
"""
['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies',
 'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance'
, 'science_fiction']
"""
```
#### 路透社语料库
10788个新闻文档,130万字,90个主题,按照"训练"和"测试"分为2组
```python
from nltk.corpus import reuters
reuters.fileids()
"""
['test/14826', 'test/14828', 'test/14829', 'test/14832', 'test/14833', 'test/148
39', 'test/14840', 'test/14841', ...]
"""
```
#### 就职演说语料库
```python
from nltk.corpus import inaugural
```

#### 标注文本语料库
语言学标注:
- 词性标注
- 命名实体
- 句法结构
- 语义角色

> NLTK中的一些语料库和语料库样本参见
[http://www.nltk.org/nltk_data/](http://www.nltk.org/nltk_data/)

#### 其他语言的语料库
"世界人权宣言"udhr

#### 文本语料库的结构

> 表2-3 NLTK中定义的基本语料库函数(略)

`help(nltk.corpus.reader)`

或查阅

[http://www.nltk.org/howto/corpus.html](http://www.nltk.org/howto/corpus.html)

#### 载入你自己的语料库
- PlaintextCorpusReader
```python
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'F:\workspace\pycharm\nlp_corpus\project_data\history\201904091317'
file_pattern = r'.*'
wordlists=PlaintextCorpusReader(corpus_root,file_pattern)
wordlists.fileids()
"""
['abstract.txt', 'pubmed_exist_id.txt', 'pubmed_info.txt', 'pubmed_miss_id.txt']
"""
 
```
- BracketParseCorpusReader
```python
from nltk.corpus import BracketParseCorpusReader
corpus_root = r'F:\workspace\pycharm\nlp_corpus\project_data\history\201904091317'
file_pattern = r'.*'
wordlists=BracketParseCorpusReader(corpus_root,file_pattern)
wordlists.fileids()
"""
['abstract.txt', 'pubmed_exist_id.txt', 'pubmed_info.txt', 'pubmed_miss_id.txt']
"""
 
```
### 2.2 条件频率分布
 
#### 条件和事件
条件频率分布需要给每个事件关联一个条件,   
处理一系列配对序列(不是处理一个词序列)  
每对的形式:(条件,事件)
#### 按文本计数词汇
- `FreqDist()` 以一个简单的链表作为输入
- `ConditionalFreqDist()` 以一个配对链表作为输入

```python
import nltk
from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(
		(genre,word)
		for genre in brown.categories()
		for word in brown.words(categories=genre)
		)
```
#### 绘制分布图和分布表
在`plot()`和`tabulate()`方法中,	   
可以使用 `conditions=`参数指定现实哪些条件
可以使用 `samples=`参数来限制要显示的样本

```python
import nltk
from nltk.corpus import inaugural

cfd = nltk.ConditionalFreqDist(
		(target,fileid[:4])
		for fileid in inaugural.fileids()
		for w in inaugural.words(fileid)
		for target in ['america','citizen']
		if w.lower().startswith(target))
cfd
"""<ConditionalFreqDist with 2 conditions>"""

cfd['america']
"""
FreqDist({'1993': 33, '1997': 31, '2005': 30, '1921': 24, '1973': 23, '1985': 21
, '2001': 20, '1981': 16, '2009': 15, '1909': 12, ...})
"""

cfd['citizen']
"""
FreqDist({'1841': 38, '1821': 15, '1817': 14, '1885': 13, '1889': 12, '1929': 12
, '1845': 11, '2001': 11, '1805': 10, '1893': 10, ...})
"""

cfd['citizen']['1841']
"""38"""
```

```python
import nltk
from nltk.corpus import udhr
languages = ['Chickasaw','English','German_Deutsch','Greenlandic_Inuktikut','Hungarian_Magyar','Ibibio_Efik']
cfd = nltk.ConditionalFreqDist(
	(lang,len(word))
	for lang in languages
	for word in udhr.words(lang+'-Latin1'))
cfd.tabulate(conditions=['English','German_Deutsch'],
	samples=range(10), cumulative=True)	
"""
                  0    1    2    3    4    5    6    7    8    9
       English    0  185  525  883  997 1166 1283 1440 1558 1638
German_Deutsch    0  171  263  614  717  894 1013 1110 1213 1275
"""	
```
#### 使用双联词生成随机文本

`bigrams()`函数接受一个词汇链表,并建立一个连续的词对链表

选择一个词作为初始内容--种子词

将每个词作为一个条件,对于每个词都有效地依据后续词的创建频率分布

`缺点`:这种简单的文本生成方法会在循环中卡主

`改进`:在可用的词汇中随机选择下一个词

### 2.3 更多关于 Python: 代码重用(略)
#### 使用文本编辑器创建程序
#### 函数
#### 模块
### 2.4 词典资源
`词项`包括`词目`(也叫`词条`)及其他`附加信息`。

两个含义不同但拼写想同的分词被称为同音异义词。
#### 词汇列表语料库

目的:过滤文本

- 词汇语料库是 `UNIX` 中的`/usr/dict/words`文件,
	- `from nltk.corpus import words`
	- `words.words()`
- 停用词语料库 
	- `from nltk.corpus import stopwords`
	- `stopwords.words("english")`
- 名字词语料库 
	- `from nltk.corpus import names`
	- `names.words('male.txt'),names.words('female.txt'),`
#### 发音的词典
表格(或电子表格)在每一行中含有一个词及其一些性质

NLTK中包括美国英语的 CMU 发音词典,它是为语音合成器而设计的

- `from nltk.corpus import cmudict`
- `cmudict.entries()`

任意一个词,词典资源都有语音的代码(不同的声音有着不同的标签,称为音素)

CMU 发音词典中的符号是从 Arpabet 来的,详情参考[https://en.wikipedia.org/wiki/ARPABET](https://en.wikipedia.org/wiki/ARPABET)