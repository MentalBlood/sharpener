from math import sqrt



def benchmark_sqrt(n):
	[sqrt(i) for i in range(n)]


def benchmark_sqr(n):
	[i ** 2 for i in range(n)]


def benchmark_power(a, n):
	a ** n