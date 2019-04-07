# genostack
项目练习





## 项目日志
- 安装 biopython,可以对 pubmed 数据库进行处理
```
pip install biopython
```

## 项目规划
- [ ] 基本爬虫功能
    -[ ] 关键字查询，返回 pmid 列表
    -[ ] 通过 pmid 列表，展示摘要（title）
    -[ ] 通过 pmid 批量下载
- [ ] 希望增加 ui 界面，处理
    -[ ] 用户交互
    -[ ] 路径参数配置 
    
## 参考链接

[Marco Bonzanini:Searching PubMed with Python](https://marcobonzanini.com/2015/01/12/searching-pubmed-with-python/)

[billgreenwald:Pubmed-Batch-Download](https://github.com/billgreenwald/Pubmed-Batch-Download)

-----
暂时存放一下

# python 模版
```python
##!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : ${DATE} ${TIME}
# @Author : ${USER}
# @Email : ice-melt@outlook.com
# @File : ${NAME}.py
# @Project : ${PROJECT_NAME}
```
其他可用的预定义文件模板变量为：
```bash
$ {PROJECT_NAME} - 当前项目的名称。
$ {NAME} - 在文件创建过程中在“新建文件”对话框中指定的新文件的名称。
$ {USER} - 当前用户的登录名。
$ {DATE} - 当前的系统日期。
$ {TIME} - 当前系统时间。
$ {YEAR} - 今年。
$ {MONTH} - 当月。
$ {DAY} - 当月的当天。
$ {HOUR} - 目前的小时。
$ {MINUTE} - 当前分钟。
$ {PRODUCT_NAME} - 将在其中创建文件的IDE的名称。
$ {MONTH_NAME_SHORT} - 月份名称的前3个字母。 示例：1月，2月等
$ {MONTH_NAME_FULL} - 一个月的全名。 示例：1月，2月等
```
