#!/usr/bin/python3
#coding=utf-8
def if_esxit(the_list,find_txt):
	for item in the_list:
		if item == find_txt:
			print(find_txt,"is in list")
if __name__ == '__main__':
	if_esxit(['a','b','c','d'],'c')
