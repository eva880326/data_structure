from util import *
print_header()
val = eval(input('\n輸入搜尋鍵值: '))

def interpolation_search():
	low, high = 0, len(data)-1

	while low <= high:
		if val < data[low] or val > data[high]:
			return -1
		ratio = (val-data[low]) / (data[high]-data[low])
		rank = ratio * (high-low)
		index = low + int(rank)

		if val < data[index]:
			high = index - 1
		elif val > data[index]:
			low = index + 1
		else:
			return index
	return -1

found = interpolation_search()
if found != -1:
	print("找到", val, "的索引值為", found)
else:
	print("找不到", val)
