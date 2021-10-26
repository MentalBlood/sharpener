from math import sqrt
from sharpener import Benchmark



class benchmark_sqrt(Benchmark):

	def run(self, n):
		[sqrt(i) for i in range(n)]


class benchmark_sqr(Benchmark):

	def run(self, n):
		[i ** 2 for i in range(n)]


class benchmark_power(Benchmark):

	def run(self, a, n):
		a ** n