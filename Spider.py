# -*- coding: utf-8 -*-
"""
@Time    : 2021/11/21 22:01
@Author  : AI悦创
@FileName: Spider.py
@Software: PyCharm
@Blog    ：https://www.aiyc.top
@公众号   ：AI悦创
@description：
1. 抓取笔趣阁的大主宰小说：http://www.b520.cc/0_7/ √
2. 抓取目录：title：link 保存到 当前路径下的 data 文件夹里面的 directory.txt/story_information.txt √
3. 进入详情页（文章内容页）抓取小说 保存到当前路径下的 data 文件夹里面的 content 文件夹里面
每个一个文件：
- 文件名称：章节名称
- 文件内容：小说内容
4. Plus 把代码写成类——课后作业
"""
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import time

story_title = ""
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", }


def crawler(url):
	try:
		html = requests.get(url, headers=headers)
		if html.status_code == 200:
			return html.text
		else:
			return "None"
	except RequestException as e:
		return e


def parse_directory(html):
	global story_title
	soup = BeautifulSoup(html, "lxml")
	story_title = soup.select("#info h1")[0].string
	directorys = soup.select("#list dl dd a")[9:]
	# print(directory)
	for dir in directorys:
		href = dir.get("href")
		chapter_title = dir.string
		yield {
			"href": href,
			"chapter_title": chapter_title
		}


def parse_detail_content(htmls):
	for html in htmls:
		detail_content_url = html.get("href", "https://www.aiyc.top")
		# print(detail_content_url)
		time.sleep(1)
		# print(detail_content_url)
		html = crawler(detail_content_url)
		soup = BeautifulSoup(html, "lxml")
		detail_content_title_lst = soup.select(".box_con .bookname h1")
		if detail_content_title_lst:
			detail_content_title = detail_content_title_lst[0].string.strip()
		# print(detail_content_title)
		contents = soup.select("#content")[0].select("p")
		# print(contents, end="\n\n\n\n")
		content_text = ""
		for content in contents:
			# print(content.string.strip())
			content = content.string.strip()
			content_text += content
			# content_text = content_text + content
			# print(content_text)
		yield {
			"detail_content_title": detail_content_title,
			"content_text": content_text
		}
		# print(content.text)


def save(content, filename):
	with open(filename, "a+", encoding="utf-8") as f:
		f.write(content)


def main():
	home_url = "http://www.b520.cc/0_7/"
	html = crawler(home_url)
	content = list(parse_directory(html))
	# print(story_title)
	for i in content:
		save(str(i) + "\n", "data/story_information{}.txt".format(story_title))
	r = parse_detail_content(content)
	for index, i in enumerate(r):
		# print(i)
		content_old = i.get("content_text", "default_content")
		content = content_old.split("。")
		page_title = i.get('detail_content_title', 'default_name').replace(" ", "").replace("【", "").replace("】", "")
		for con in content:
			# save(con + "。\n", f"data/content/{f'{index+1}' + i.get('detail_content_title', 'default_name')}.md")
			save(con + "。\n", f"data/content/{index+1}{page_title}.md")

if __name__ == '__main__':
	# 快速优化、快速熟悉代码
	main()
