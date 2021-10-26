from sharpener import Benchmark



class benchmark_index(Benchmark):

	def run(self, l, e):
		l.index(e)