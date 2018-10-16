"""
Recursive fibonacci sequence
"""

#print("This program calcuates number of ways to ascend a given number of stairs with a combination of 1, 2, or 3 steps")
#user_input = input("Please enter number of stairs: ")

fibonacci_cache = {}

def fibonacci(n):
	value = 0
	if n == 1:
		value = 1
	elif n == 2:
		value = 1
	elif n > 2:
		value = fibonacci(n-1) + fibonacci(n-2)

	#cache the value and return it
	fibonacci_cache[n] = value
	return value

#for n in range (1,100):
#	print(n, ":", fibonacci(n))
