# -*- coding: utf-8 -*-
# Fibonacci numbers module

def fibo(n):	# Write Fibonacci series up to n
	a, b = 0, 1
	while b < n:
		print b,
		a, b = b, a+b

def fibo2(n):	# return Fibonacci series up to n
	result = []
	a, b = 0, 1
	while b < n:
		result.append(b)
		a, b = b, a+b

	return result

