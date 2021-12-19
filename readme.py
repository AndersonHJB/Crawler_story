# -*- coding: utf-8 -*-
"""
@Time    : 2021/12/12 23:24
@Author  : AI悦创
@FileName: readme.py
@Software: PyCharm
@Blog    ：https://www.aiyc.top
@公众号   ：AI悦创
@description：
"""
import os
import re


# def regex_num(filename_list):
# 	pattern = re.compile("\d")
# 	for filename in filename_list:
# 		content = re.search(pattern, filename, re.S)
# 	return content

def regex_num(filename_list):
	sort_lst = []
	# pattern = re.compile("\d")
	for index, filename in enumerate(filename_list):
		print(filename)
		# if filename.startswith(f"{index+1}"):
		if str(index+1) in filename:
			sort_lst.append(filename)
		else:
			pass
	return sort_lst
from pprint import pprint
# ./data/content/100第九十七章 灵轮境后期.md"
# [100第九十七章 灵轮境后期.md](./data/content/100第九十七章 灵轮境后期.md)
def readme():
	path = os.walk("./data/content/")
	# print(list(r))
	with open("README.md", "w+", encoding="utf-8") as f:
		f.write("# 大主宰\n")
		for root, file, filename_list in path:
			# pprint(i)
			# print(type(filename_list))
			# filename_list.sort()
			# filename = sorted(filename_list)
			# print(filelist)
			r = regex_num(filename_list)
			print(r)
			# for file in r:
			# # for file in filename_list:
			# 	r = os.path.join(root, file)
			# 	print(r)
			# 	f.write(f"[{file}]({r})\n\n")
	# with open()

if __name__ == "__main__":
	readme()