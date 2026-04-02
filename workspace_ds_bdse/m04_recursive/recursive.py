def up_and_down(n):
	print("level", n)
	if n < 4:
		up_and_down(n+1)
	print("LEVEL", n)

up_and_down(1)
