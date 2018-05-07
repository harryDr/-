#coding=utf-8
#查找方法 分别为顺序查找、二分查找、分块查找
#顺序查找就是遍历整个数组 找到则返回
# 时间复杂度O(n)
def order_search(list1,key):
	for i in range(len(list1)):
		if list1[i] == key:
			print ('在%d处找到，值为%d' % (i+1, list1[i]))
			return True
	print ('没有找到')
	return False

if __name__ == '__main__':
	a = [1,3,2,7,4,8,5,9]
	order_search(a,8)