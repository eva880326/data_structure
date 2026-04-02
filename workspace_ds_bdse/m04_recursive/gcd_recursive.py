def gcd(dividend, divisor):
	if divisor != 0:
		remainder = dividend % divisor
		return gcd(divisor, remainder)
	else:
		return dividend


print("gcd =", gcd(123, 36))
print("gcd =", gcd(36, 123))
