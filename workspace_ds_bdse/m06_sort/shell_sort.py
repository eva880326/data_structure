from util import *

def shell_sort():
	gap, count = 3, 1
	while gap >= 1:
		for g in range(gap):
			for i in range(g+gap, len(data), gap):
				temp = data[i]
				for j in range(i-gap, -1, -gap):
					if data[j] > temp:
						data[j+gap] = data[j]
						data[j] = temp
					else:
						break

		print("\n第", count, "回合", sep="", end="")
		for k in range(len(data)):
			print("%4d" % data[k], end="")
		gap -= 1
		count += 1

print_header()
shell_sort()
