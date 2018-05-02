#coding=utf-8
import random
#插入排序算法 从数组的第一个数开始排序，数组右边的为待插入的数据
#插入时与前一个相比较形成有序序列
def insert_sort(listl):
	for i in range(1,len(listl)):
		key = listl[i]
		j = i-1
		while j >= 0:
			if listl[j] > key:
				listl[j+1] = listl[j]
				listl[j] = key
			j -= 1
	return listl

#冒泡排序   (交换排序)
# 遍历n-1次 每次遍历找出最大或者最小的数
def maopao_sort(list1):
	for i in range(len(list1)-1):
		for j in range (i,len(list1)):
			if list1[i] > list1[j]:
				list1[i],list1[j] = list1[j],list1[i]
	return list1

#快速排序   (交换排序)  需要继续理解
# 1、先从数列中取出一个数作为基准数
# 2、分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边
# 3、再对左右区间重复第二步，直到各区间只有一个数
def quick_sort(list1,l,r):
	i = l
	j = r
	if i >= j:
		return list1
	key = list1[i]
	while i < j:
		while i < j and list1[j] >= key:
			j -= 1
		list1[i] = list1[j]
		while i < j and list1[i] <= key:
			i += 1
		list1[j] = list1[i]
	list1[i] = key
	quick_sort(list1, l, i - 1)
	quick_sort(list1, j + 1, r)
	return list1

#简单选择排序 （选择排序）
#每一趟在n-i+1（i=1，2，…n-1）个记录中选取关键字最小的记录作为有序序列中第i个记录
# (关键是取出每趟中的最小值 进行交换)
def select_sort(list1):
	for i in range(len(list1)-1):
		key = i
		for j in range(i+1,len(list1)):
			if list1[key] > list1[j]:
				key = j
		list1[i],list1[key] = list1[key],list1[i]
	return list1

if __name__ == '__main__':
	a= [random.randint(1, 1000) for i in range(20)]
	insert_sort(a)
	# maopao_sort(a)
	# quick_sort(a,0,len(a)-1)
	# select_sort(a)
	print(a)