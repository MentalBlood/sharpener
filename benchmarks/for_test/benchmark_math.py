from math import sqrt
from sharpener import Benchmark



class Sqrt(Benchmark):

	def run(self, n):
		[sqrt(i) for i in range(n)]


class Sqr(Benchmark):

	def run(self, n):
		[i ** 2 for i in range(n)]


class Power(Benchmark):

	def run(self, a, n):
		a ** n