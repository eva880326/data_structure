def precede(c):
	if c == '/' or c == '*':
		return 2
	elif c == '+' or c == '-':
		return 1
	else:
		return -1

def to_postfix(expr):
	result = ""
	stack = []
	for i in range(len(expr)):
		c = expr[i]
		if 'a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9':
			result += c
		elif c == '(':
			stack.append(c)
		elif c == ')':
			while len(stack) > 0 and stack[-1] != '(':
				result += stack.pop()
			stack.pop()  # Pop'('
		else:
			while len(stack) > 0 and precede(c) <= precede(stack[-1]):
				result += stack.pop()
			stack.append(c)

	while len(stack) > 0:
		result += stack.pop()
	return result

expr_ = "A-B*(C+D)/E"
print(to_postfix(expr_))  # ABCD+*E/-
expr_ = "A+B-C*(D+E)/F"
print(to_postfix(expr_))  # AB+CDE+*F/-
