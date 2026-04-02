def factorial(n):
	result = 1
	for i in range(n, 1, -1):
		result *= i
	return result

num = eval(input('Input a number: '))
print("factorial =", factorial(num))
