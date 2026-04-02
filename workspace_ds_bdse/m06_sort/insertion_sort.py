from util import *

def insertion_sort():
	for i in range(1, len(data)):
		temp = data[i]
		for j in range(i-1, -1, -1):
			if data[j] > temp:
				data[j+1] = data[j]
				data[j] = temp
			else:
				break
		print("\n第", i, "回合", sep="", end="")
		for k in range(len(data)):
			print("%4d" % data[k], end="")

print_header()
insertion_sort()
