#coding=utf-8
import random
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
	a= [random.randint(1, 1000) for i in range(10)]
	print(a)
	print(select_sort(a))