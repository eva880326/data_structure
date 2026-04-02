def gcd(dividend, divisor):
	while divisor != 0:
		remainder = dividend % divisor
		dividend = divisor
		divisor = remainder
	return dividend


print("gcd =", gcd(123, 36))
print("gcd =", gcd(36, 123))
