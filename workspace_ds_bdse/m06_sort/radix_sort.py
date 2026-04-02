data = [73, 365, 5, 924, 8563, 1117, 3325, 97, 41, 19]

def radix_sort():
	length = len(str(max(data)))
	# 定義一個list,裡面有10個list,代表10個桶
	bucket = [[] for _ in range(10)]

	# 針對每個元素的各位數進行排序處理
	n = 1
	for i in range(length):
		for j in range(len(data)):
			# 取出每個元素的的對應位數的值
			digit = data[j] // n % 10
			# 放入到對應的桶中
			bucket[digit].append(data[j])

		# 遍歷每個桶,並將桶中資料放入到原陣列
		index = 0
		for j in range(10):
			# 如果桶中有資料才放入到原陣列
			if len(bucket[j]) != 0:
				for k in range(len(bucket[j])):
					data[index] = bucket[j].pop(0)
					index += 1

		print("\n第", i + 1, "回合", sep="", end="")
		for k in range(len(data)):
			print("%5d" % data[k], end="")
		n *= 10

print("陣列     [0]  [1]  [2]  [3]  [4]  [5]  [6]  [7]  [8]  [9]")
print("---------------------------------------------------------")
print("排序前:", end="")
for s in range(len(data)):
	print("%5d" % data[s], end="")
print(" ")
radix_sort()
