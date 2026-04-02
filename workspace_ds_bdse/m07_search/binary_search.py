from util import *

def binary_search(val):
	low, high = 0, len(data)-1
	while low <= high:
		mid = (low + high) // 2
		if val < data[mid]:
			high = mid - 1
		elif val > data[mid]:
			low = mid + 1
		else:
			return mid
	return -1

print_header()
value = eval(input('\n輸入搜尋鍵值: '))
found = binary_search(value)
if found != -1:
	print("找到", value, "的索引值為", found)
else:
	print("找不到", value)
