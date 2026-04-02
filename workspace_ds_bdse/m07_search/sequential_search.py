data = [73, 65, 52, 24, 83, 17, 35, 96, 41, 9]
print("陣列     [0] [1] [2] [3] [4] [5] [6] [7] [8] [9]")
print("------------------------------------------------")
print("排序前:", end="")
for i in range(len(data)):
	print("%4d" % data[i], end="")
print(" ")
val = eval(input('\n輸入搜尋鍵值: '))

def sequential_search():
	for j in range(len(data)):
		if data[j] == val:
			return j
	return -1

found = sequential_search()
if found != -1:
	print("找到", val, "的索引值為", found)
else:
	print("找不到", val)
