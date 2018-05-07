#coding=utf-8
import random
#快速排序   (交换排序)  需要继续理解
# 1、先从数列中取出一个数作为基准数
# 2、分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边
# 3、再对左右区间重复第二步，直到各区间只有一个数
def quick_sort(list1,l,r):
	i,j = l,r
	if i >= j:
		return list1
	key = list1[i]
	while i < j :
		while i<j and list1[j]>key:
			j -= 1
		while i<j and list1[i]<key:
			i += 1
		list1[j],list1[i] = list1[i],list1[j]
	# list1[i] = key
	quick_sort(list1,l,i-1)
	quick_sort(list1,i+1,r)
	return list1

#另一种实现
# def quick_sort(list1,l,r):
# 	i = l
# 	j = r
# 	if i >= j:
# 		return list1
# 	key = list1[i]
# 	while i < j:
# 		while i < j and list1[j] >= key:
# 			j -= 1
# 		list1[i] = list1[j]
# 		while i < j and list1[i] <= key:
# 			i += 1
# 		list1[j] = list1[i]
# 	list1[i] = key
# 	quick_sort(list1, l, i - 1)
# 	quick_sort(list1, j + 1, r)
# 	return list1
if __name__ == '__main__':
	a= [random.randint(1, 1000) for i in range(10)]
	print(a)
	print(quick_sort(a,0,len(a)-1))
