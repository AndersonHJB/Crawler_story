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
from pprint import pprint
# ./data/content/100第九十七章 灵轮境后期.md"
# [100第九十七章 灵轮境后期.md](./data/content/100第九十七章 灵轮境后期.md)
def readme():
	path = os.walk("./data/content/")
	# print(list(r))
	with open("README.md", "w+", encoding="utf-8") as f:
		for root, file, filename_list in path:
			# pprint(i)
			# print(type(filename_list))
			filename_list.sort()
			# print(filelist)
			for file in filename_list:
				r = os.path.join(root, file)
				print(r)
				f.write(f"[{file}]({r})\n")
	# with open()

if __name__ == "__main__":
	readme()