from util import *

print_header()
val = eval(input('\n輸入搜尋鍵值: '))

def fibonacci_search():
	n = find_n()
	fib = create_fibonacci(n+1)

	idx = fib[n]-1
	if val > data[idx]:
		idx = len(data) - 1

	result = -1
	n -= 1
	while fib[n] >= 1:
		if val < data[idx]:
			n -= 1
			idx -= fib[n]
		elif val > data[idx]:
			n -= 1
			idx += fib[n]
		else:
			result = idx
			break
	return result

def find_n():
	n = 0
	while fibonacci(n) <= len(data):
		n += 1
	n -= 1
	return n

def fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	prev1 = 0
	prev2 = 1
	for i in range(2, n+1):
		temp = prev2
		prev2 = prev1 + prev2
		prev1 = temp
	return prev2

def create_fibonacci(length):
	fib = [0]*length
	fib[0] = 0
	fib[1] = 1
	for i in range(2, len(fib)):
		fib[i] = fib[i-1] + fib[i-2]
	return fib

found = fibonacci_search()
if found != -1:
	print("找到", val, "的索引值為", found)
else:
	print("找不到", val)
