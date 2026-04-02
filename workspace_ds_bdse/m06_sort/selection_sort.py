from util import *

def selection_sort():
	for i in range(len(data) - 1):
		min_ = i
		for j in range(i+1, len(data)):
			if data[j] < data[min_]:
				min_ = j
		temp = data[i]
		data[i] = data[min_]
		data[min_] = temp

		print("\n第", i + 1, "回合", sep="", end="")
		for k in range(len(data)):
			print("%4d" % data[k], end="")

print_header()
selection_sort()
