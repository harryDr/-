#coding=utf-8
#二分查找是一个排序好的数组 比较查找的值与中间的值的大小确定查找输的范围
#二分法比较适用于顺序存储结构  顺序结构中插入和删除都必须移动大量的结点
# 时间复杂度为 O(log2 n)  空间复杂度O(1)
def binary_search(list1,key):
	left,right = 0, len(list1)-1
	while left<right:
		mid = int((left+right)/2)
		if list1[mid]>key:
			right = mid-1
		elif list1[mid]<key:
			left = mid+1
		else:
			print ('在%d处找到，值为%d' % (mid + 1, list1[mid]))
			return True
	print ('没有找到！')
	return False

if __name__ == '__main__':
	a = [2,4,6,9,12]
	binary_search(a,9)