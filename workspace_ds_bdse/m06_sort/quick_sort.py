from util import *
step = 0

def quick_sort(low, high):
	global step
	if low < high:
		divide_point = divider(low, high)
		step += 1
		print("\n第", step, "回合", sep="", end="")
		for i in range(len(data)):
			print("%4d" % data[i], end="")
		quick_sort(low, divide_point-1)
		quick_sort(divide_point+1, high)

def divider(low, high):
	i, j = low+1, high
	pivot = data[low]
	while True:
		while data[i] < pivot and i < high:  # 向右找第一個比pivot大的值的所在位置
			i += 1
		while data[--j] > pivot and j > low:  # 向左找第一個比pivot小的值的所在位置
			j -= 1
		if i < j:
			temp = data[i]
			data[i] = data[j]
			data[j] = temp
		else:
			break
	temp = data[low]
	data[low] = data[j]
	data[j] = temp
	return j

print_header()
quick_sort(0, len(data)-1)
