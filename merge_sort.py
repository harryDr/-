#coding=utf-8
import random
#归并排序  分治法的一个典型应用
#创建在归并操作上的一种有效的排序算法，效率为 O(nlogn)
#原理：将序列中每相连的两个数字进行归并，排序后的每个序列包含两个元素，将此序列再次归并.
#直到所有元素排序完毕
def merge_sort(list1):
	if len(list1)<=1:   #拆分为单个元素的时候就不在拆分了
		return list1
	mid = int(len(list1)/2)
	left = merge_sort(list1[:mid])
	right = merge_sort(list1[mid:])
	return merge(left,right)

def merge(left,right):
	l,r = 0,0
	result = []
	while l<len(left) and r<len(right):
		if left[l] < right[r]:
			result.append(left[l])
			l+=1
		else:
			result.append(right[r])
			r+=1
	result += left[l:]
	result += right[r:]
	return result



if __name__ == '__main__':
	a= [random.randint(1, 1000) for i in range(10)]
	print(a)
	print(merge_sort(a))