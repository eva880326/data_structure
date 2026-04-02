from util import *

def heap_sort():
	high_index = len(data) - 1
	create_maxheap(high_index)
	count = 1
	for i in range(len(data)-1, -1, -1):
		# 將leaf node最右邊那個跟根節點交換
		temp = data[i]
		data[i] = data[0]
		data[0] = temp
		print("\n第", count, "回合", sep="", end="")
		for k in range(len(data)):
			print("%4d" % data[k], end="")
		count += 1
		high_index -= 1
		# 此時根節點並非最大值 需要執行max_heapify
		heapify(0, high_index)

def create_maxheap(high_index):
	# 從(high_index-1)//2這個節點開始檢查
	for i in range((high_index-1)//2, -1, -1):
		heapify(i, high_index)

def heapify(i, high_index):
	left = i * 2 + 1
	right = i * 2 + 2
	# 檢查subtree裡面誰是最大值?
	largest = left if left <= high_index and data[left] > data[i] else i
	if right <= high_index and data[right] > data[largest]:
		largest = right

	# 如果subtree的parent不是最大的,就持續向下交換
	if largest != i:
		temp = data[i]
		data[i] = data[largest]
		data[largest] = temp
		heapify(largest, high_index)

print_header()
heap_sort()
