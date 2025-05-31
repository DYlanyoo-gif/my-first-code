# 轻量级新闻头条聚合器 (Simple News Headline Aggregator)

## 📝 项目简介

这是一个使用 Python、`requests` 库和 `BeautifulSoup4` 库编写的简单新闻头条爬虫。
主要目的是练习基本的网页抓取和HTML解析技术，并能够从几个指定的新闻网站聚合最新的新闻标题和链接，方便快速浏览。

这个项目是在学习过程中逐步完成的。

## ✨ 主要功能

* 从多个预设的新闻网站抓取最新的新闻头条。
* 提取每条新闻的标题和对应的URL链接。
* 在终端清晰地打印输出抓取到的新闻列表。

目前支持的新闻源包括：
* BBC 中文网
* 百度-热搜榜
* 环球网
* 联合早报
* (你可以继续添加你实际爬取的网站)

## 🛠️ 技术栈

* Python 3.12.4 
* `requests` (用于发送HTTP请求)
* `BeautifulSoup4` (用于解析HTML内容)

## 🚀 如何运行

### 1. 环境准备

* 确保你已安装 Python 3 (本项目基于 Python 3.12+ 开发)。
* 克隆或下载本项目到你的本地。

### 2. 安装依赖

在项目根目录下 (即 `Newspider` 文件夹内)，打开终端或命令行，运行以下命令来安装所需的库：
```bash
pip install -r requirements.txt
3. 运行脚本
安装完依赖后，通过以下命令运行爬虫 ：

Bash

python newspider.py

📋 运行效果示例
以下是程序在终端成功运行并输出新闻的典型结果：

Plaintext

--- 正在抓取【BBC 中文网】的新闻头条 ---
  1. “哈佛难民”的五月过山车：有中国学生“已经在看机票准备离开”
     链接: [https://www.bbc.com/zhongwen/articles/cvgn1nyqp20o/simp](https://www.bbc.com/zhongwen/articles/cvgn1nyqp20o/simp)
  2. 中美贸易90天停战期间怎么谈判？红线、筹码与突破口
     链接: [https://www.bbc.com/zhongwen/articles/c7v7ml1083mo/simp](https://www.bbc.com/zhongwen/articles/c7v7ml1083mo/simp)
  3. 香格里拉对话前瞻：中美军队争夺亚太安全主导权
     链接: [https://www.bbc.com/zhongwen/articles/cvgv1xrvdlvo/simp](https://www.bbc.com/zhongwen/articles/cvgv1xrvdlvo/simp)
  4. 因两年前匿名发表“极端言论”，中国女子遭举报并被取消“考公”资格
     链接: [https://www.bbc.com/zhongwen/articles/cn7zkd4282po/simp](https://www.bbc.com/zhongwen/articles/cn7zkd4282po/simp)
  5. 世界首富马斯克以哪五种方式改变了美国白宫
     链接: [https://www.bbc.com/zhongwen/articles/cwy6lqv5yydo/simp](https://www.bbc.com/zhongwen/articles/cwy6lqv5yydo/simp)
  6. 中国学者称“小红书治理台湾”引热议，台湾年轻人会被“统战”吗？
     链接: [https://www.bbc.com/zhongwen/articles/c5y5qlegqndo/simp](https://www.bbc.com/zhongwen/articles/c5y5qlegqndo/simp)
  7. 印巴相争中国得利？中国官方保持低调难掩全球军售变局
     链接: [https://www.bbc.com/zhongwen/articles/c23m18mv7rro/simp](https://www.bbc.com/zhongwen/articles/c23m18mv7rro/simp)
  8. 美国签证禁令：国际学生还有哪些选择？
     链接: [https://www.bbc.com/zhongwen/articles/c1mg8vxj9v8o/simp](https://www.bbc.com/zhongwen/articles/c1mg8vxj9v8o/simp)
  9. 美国国务院：将撤销中国学生签证，加强对中国及香港申请人审查
     链接: [https://www.bbc.com/zhongwen/articles/c0k3d5yjz11o/simp](https://www.bbc.com/zhongwen/articles/c0k3d5yjz11o/simp)
  10. 美国上诉法院裁定特朗普关税措施目前可继续实施
      链接: [https://www.bbc.com/zhongwen/articles/cr4zd9n639xo/simp](https://www.bbc.com/zhongwen/articles/cr4zd9n639xo/simp)

(此处可以继续添加其他网站的示例输出)

🔮 未来展望
考虑使用 Scrapy 框架进行更复杂和大规模的爬取。
为项目添加一个简单的图形用户界面 (GUI)。
将爬取的数据存储到数据库中
