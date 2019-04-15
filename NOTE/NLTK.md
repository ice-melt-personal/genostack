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

```python
print([w for w, pron in entries if pron[-1] == 'M' and w[-1] == 'n'])
print(sorted(set(w[:2] for w, pron in entries if pron[0] == 'N' and w[0] != 'n')))
"""
['autumn', 'column', 'condemn', 'damn', 'goddamn', 'hymn', 'solemn']
['gn', 'kn', 'mn', 'pn']
"""
```

**音素**包含数字表示
- 主重音(1)
- 次重音(2)
- 无重音(0)
```python
def stress(pron):
	return [char for phone in pron for char in phone if char.isdigit()]

entries = nltk.corpus.cmudict.entries()
print([w for w, pron in entries if stress(pron) == ['0', '1', '0', '2', '0']])
"""
['abbreviated', 'abbreviated', 'abbreviating', ...]
"""
```
通过指定词典的名字及后面带方括号的**关键字**来查词典

- `prondict = nltk.corpus.cmudict.dict()`
- `prondict['fire']`
#### 比较词表
词典表格的另一例子是比较词表

NLTK中包含**斯瓦迪士核心词列表**(`Swadesh wordlists`),
- 包括几种语言的约200个常用词列表
- 语言标识符使用 ISO639双字母码

核心词语料库
- `from nltk.corpus import swadesh`
- 指定一个语言链表来访问多语言中的同源词,或转换成一个简单的词典
- `fr2en = swadesh.entries('fr','en')`
#### 词汇工具:Toolbox 和 Shoebox

Toolbox下载:[https://software.sil.org/toolbox/](https://software.sil.org/toolbox/)
- 罗托卡特语(Rotokas)词典
```python
from nltk.corpus import toolbox
toolbox.entries('rotokas.dic')
"""
[('kaa', [('ps', 'V'), ('pt', 'A'), ('ge', 'gag'), ('tkp', 'nek i pas'), ('dcsv', 'true'), ('vx', '1'), ('sc', '???'), ('dt', '29/Oct/2005'), 
('ex', 'Apoka irakaaroi aioa-ia reoreopaoro.'), 
('xp', 'Kaikai i pas long nek bilong Apoka bikosem i kaikai na toktok.'), 
('xe', 'Apoka is gagging from food while talking.')]),...]
"""
# ('ps','V')-词性是'V'(动词)
# ('ge', 'gag')-英文注释是'gag'
# ex-罗托卡特语例句;xp,xe-巴布亚皮欣语和英语的翻译

```
- Toolbox文件由一些条目的集合组成,
- 其中每个条目由一个或多个字段组成.
- 大多数字段都是可选的或重复的
- 这个词汇资源不能作为一个表格或电子表格来处理
- 条目包括一系列"属性-值"对
### 2.5 WordNet
wordnet 是面向语义的英语词典

#### 意义与同义词
```python
from nltk.corpus import wordnet
wordnet.synsets('motorcar')  # car的第一个名词意义
wordnet.synset('car.n.01').lemma_names()  # 同义词集
wordnet.synset('car.n.01').definition()  # 词集定义
wordnet.synset('car.n.01').examples()  # 词集例句
"""
[Synset('car.n.01')]
['car', 'auto', 'automobile', 'machine', 'motorcar']
a motor vehicle with four wheels; usually propelled by an internal combustion engine
['he needs a car to get to work']
"""
```

为消除歧义,将这些词标注为`car.n.01.automobile`,`car.n.01.motorcar`等

这种同义词集和词的配对叫做**词条**
- `wordnet.synset('car.n.01').lemmas()`  # 指定同义词集的所有词条
> [Lemma('car.n.01.car'), Lemma('car.n.01.auto'), Lemma('car.n.01.automobile'), Le
mma('car.n.01.machine'), Lemma('car.n.01.motorcar')]
- `wordnet.lemma('car.n.01.automobile')`  # 查找特定词条
> Lemma('car.n.01.automobile')
- `wordnet.lemma('car.n.01.automobile').synset()`  # 查找一个词条所对应的同义词集
> Synset('car.n.01')
- `wordnet.lemma('car.n.01.automobile').name()`  # 得到一个词条的名字
> 'automobile'
- `wordnet.lemmas('car')`  # 访问所有包含词car的词条
> [Lemma('car.n.01.car'), Lemma('car.n.02.car'), Lemma('car.n.03.car'), Lemma('car
.n.04.car'), Lemma('cable_car.n.01.car')]

#### WordNet 的层次结构

树状层级结构,每个节点对应一个同义词集;边表示上位词/下位词关系(即上级概念与从属概念的关系)

- 通过访问上位词来操纵层次结构
```python
from nltk.corpus import wordnet as wn
motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms()
types_of_motorcar[26]

"""Synset('stanley_steamer.n.01')"""

sorted([lemma.name() for synset in types_of_motorcar for lemma in synset.lemmas()])
"""
['Model_T', 'S.U.V.', 'SUV', 'Stanley_Steamer', 'ambulance', 'beach_waggon', 'be
ach_wagon', 'bus', 'cab', 'compact', 'compact_car', 'convertible', 'coupe', 'cru
iser', 'electric', 'electric_automobile', 'electric_car', 'estate_car', 'gas_guz
zler', 'hack', 'hardtop', 'hatchback', 'heap', 'horseless_carriage', 'hot-rod',
'hot_rod', 'jalopy', 'jeep', 'landrover', 'limo', 'limousine', 'loaner', 'minica
r', 'minivan', 'pace_car', 'patrol_car', 'phaeton', 'police_car', 'police_cruise
r', 'prowl_car', 'race_car', 'racer', 'racing_car', 'roadster', 'runabout', 'sal
oon', 'secondhand_car', 'sedan', 'sport_car', 'sport_utility', 'sport_utility_ve
hicle', 'sports_car', 'squad_car', 'station_waggon', 'station_wagon', 'stock_car
', 'subcompact', 'subcompact_car', 'taxi', 'taxicab', 'tourer', 'touring_car', '
two-seater', 'used-car', 'waggon', 'wagon']
"""
```
- `motorcar.root_hypernyms()`  # 得到一个最笼统的上位(或根上位)同义词集
- 图形化WordNet浏览器:`nltk.app.wordnet()`
#### 更多的词汇关系
- 上位词和下位词被称为**词汇关系**,是上下定位"is-a"层次
- 从条目的部件(部分)或到包含它们的东西(整体)
	- `part_meronyms()`  # 部分
	- `substance_meronyms()`  # 整体
	- `member_holonyms()`  # 集合

```python
wn.synset('tree.n.01').part_meronyms()
"""
[Synset('burl.n.02'), Synset('crown.n.07'), Synset('limb.n.02'), Synset('stump.n.01'), Synset('trunk.n.01')]
"""

wn.synset('tree.n.01').substance_meronyms()
"""[Synset('heartwood.n.01'), Synset('sapwood.n.01')]"""

wn.synset('tree.n.01').member_holonyms()
"""[Synset('forest.n.01')]"""
```	
- 单词有密切相关的意思
- 动词有多个含义
	- `wn.synset('walk.n.01').entailments()`
- 反义词
	- `wn.lemma('supply.n.02.supply').antonyms()`
- 使用dir()查看词汇关系和同义词集上定义的其他方法
	- `dir(wn.synset('harmony.n.02'))`
#### 语义相似度
如果两个同义词集公用一个特定的上位词(在上位词层次结构中属于较低层),它们一定有密切的联系


通过查找每个同义词集的深度来量化这个普遍性概念
```python
from nltk.corpus import wordnet as wn

right = wn.synset('right_whale.n.01')
orca = wn.synset('orca.n.01')
minke = wn.synset('minke_whale.n.01')
tortoise = wn.synset('tortoise.n.01')
novel = wn.synset('novel.n.01')

hypernym1, hypernym2, hypernym3, hypernym4 = (
	right.lowest_common_hypernyms(minke)
	, right.lowest_common_hypernyms(orca)
	, right.lowest_common_hypernyms(tortoise)
	, right.lowest_common_hypernyms(novel)
)

print(hypernym1, hypernym2, hypernym3, hypernym4)

depth1, depth2, depth3, depth4 = (
	wn.synset('baleen_whale.n.01').min_depth(),
	wn.synset('whale.n.02').min_depth(),
	wn.synset('vertebrate.n.01').min_depth(),
	wn.synset('entity.n.01').min_depth(),
)

print(depth1, depth2, depth3, depth4)

"""
[Synset('baleen_whale.n.01')]  # 须鲸
[Synset('whale.n.02')]  # 鲸鱼
[Synset('vertebrate.n.01')]  # 脊椎动物
[Synset('entity.n.01')]  # 实体

14 13 8 0
"""
```
基于上位词层次结构中相互关联的最短路径下的相似度方法(归一化,无路径时返回-1):
- `right.path_similarity(minke)  # return 0.25,越相似值越大,最大为1`  

> `help(wn)` 获得更多信息 
> NLTK包括 VerbNet(连接到WordNet的层次结构动词词典,`nltk.corpus.verbnet` 访问) 
## 3 处理原始文本

### 3.1 从网络和硬盘上访问文本

#### 电子书
nltk 包含 古腾堡项目 的一小部分样本文本。  
对其它文本感兴趣可访问:
[https://www.gutenberg.org/catalog/](https://www.gutenberg.org/catalog/)

此站点包含 25000 本免费在线书籍(ASCII 码文本文件)  
90%的文本是英文的,但是还包括50多种其他语言的文本材料

#### 处理HTML

- `nltk.clean_html(html)`  # 通过 html 字符串,返回原始文本

更多处理 HTML 的内容,可以下载 `Beautiful Soup` 软件包  
[https://www.crummy.com/software/BeautifulSoup/](https://www.crummy.com/software/BeautifulSoup/)

#### 处理搜索引擎的结果

- 优点:数据量大;容易使用
- 缺点:搜索方式允许的范围受到限制;搜索引擎得到的结果在异时异地不同;返回结果可能会不可预料的变化

#### 处理 RSS 订阅

- Python 库 `Universal Feed Parser` 可以访问博客内容,下载:[]()
#### 读取本地文本

