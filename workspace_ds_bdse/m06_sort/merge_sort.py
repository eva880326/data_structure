from util import *
step = 0
temp = []

def merge_sort(low, high):
	global step
	if low < high:
		mid = (low + high) // 2
		merge_sort(low, mid)
		merge_sort(mid + 1, high)
		merge(low, mid, high)
		step += 1
		print("\n第", step, "回合", sep="", end="")
		for i in range(len(data)):
			print("%4d" % data[i], end="")

def merge(low, mid, high):
	left_idx = low  # 設定左邊子序列的初始索引
	right_idx = mid + 1  # 初設定右邊子序列的初始索引

	# 左右子序列比大小,將小的放到temp列表
	while left_idx <= mid and right_idx <= high:  # 左右子序列都還沒遍歷到最後時
		if data[left_idx] <= data[right_idx]:
			temp.append(data[left_idx])
			left_idx += 1
		else:
			temp.append(data[right_idx])
			right_idx += 1

	# 把有剩餘資料的子序列依次全部放入temp
	while left_idx <= mid:  # 左子序列有剩餘的元素
		temp.append(data[left_idx])
		left_idx += 1

	while right_idx <= high:  # 右子序列有剩餘的元素
		temp.append(data[right_idx])
		right_idx += 1

	# 將temp列表的元素copy到data
	for i in range(low, high+1):
		data[i] = temp.pop(0)

print_header()
merge_sort(0, len(data)-1)
