from util import *

def bubble_sort():
	for i in range(len(data)-1):
		for j in range(len(data)-1-i):
			if data[j] > data[j+1]:
				temp = data[j]
				data[j] = data[j+1]
				data[j+1] = temp
		print("\n第", i+1, "回合", sep="", end="")
		for k in range(len(data)):
			print("%4d" % data[k], end="")

print_header()
bubble_sort()
