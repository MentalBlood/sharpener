from sharpener import Benchmark



class Index(Benchmark):

	def run(self, l, e):
		l.index(e)