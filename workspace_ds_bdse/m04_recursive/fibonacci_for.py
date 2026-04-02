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


def main():
	n = eval(input('Input a number: '))
	print("fibonacci =", fibonacci(n))

if __name__ == '__main__':
	main()
