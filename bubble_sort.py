#coding=utf-8
import random
#冒泡排序   (交换排序)
# 遍历n-1次 每次遍历找出最大或者最小的数
def bubble_sort(list1):
	for i in range(len(list1)-1):
		for j in range (i,len(list1)):
			if list1[i] > list1[j]:
				list1[i],list1[j] = list1[j],list1[i]
	return list1

if __name__ == '__main__':
	a= [random.randint(1, 1000) for i in range(10)]
	print(a)
	print(bubble_sort(a))
