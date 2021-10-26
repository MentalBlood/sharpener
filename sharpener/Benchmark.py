from functools import partial
from abc import ABC, abstractmethod



class Benchmark(ABC):

	def __init__(self, *args, **kwargs):

		for method_name in ['prepare', 'run', 'clean']:
			method = getattr(self, method_name)
			new_method = partial(method, *args, **kwargs)
			setattr(self, method_name, new_method)
	
	def prepare(self, *args, **kwargs):
		pass
	
	@abstractmethod
	def run(self, *args, **kwargs):
		pass
	
	def clean(self, *args, **kwargs):
		pass



import sys
sys.modules[__name__] = Benchmark