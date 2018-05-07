#coding=utf-8
import random
#希尔排序 (插入排序)
# 希尔排序是记录按下标的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，
# 每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。
def shell_sort(list1):
	step = int(len(list1)/2)
	while step > 0:
		for i in range(step, len(list1)):
			# 类似插入排序, 当前值与指定步长之前的值比较, 符合条件则交换位置
			while i >= step and list1[i - step] > list1[i]:
				list1[i - step],list1[i] = list1[i],list1[i - step]
				i -= step
		step = int(step / 2)
	return list1

if __name__ == '__main__':
	a= [random.randint(1, 1000) for i in range(10)]
	print(a)
	print(shell_sort(a))
