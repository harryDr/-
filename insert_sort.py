#coding=utf-8
import random
#插入排序（直接排序）算法 从数组的第一个数开始排序，数组右边的为待插入的数据
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

if __name__ == '__main__':
	a= [random.randint(1, 1000) for i in range(10)]
	print(a)
	print(insert_sort(a))