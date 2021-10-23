import glob
import importlib



class Benchmarks:

	def __init__(self, path='.'):
		
		self.path = path
		self._modules = []

		self.scan()
	
	@property
	def modules(self):
		return self._modules
	
	def scan(self):

		self._modules = []
		
		for file_path in glob.iglob(f'{self.path}/**/benchmark_*.py', recursive=True):
			
			spec = importlib.util.spec_from_file_location('module', file_path)
			module = importlib.util.module_from_spec(spec)
			spec.loader.exec_module(module)
			
			self._modules.append(module)



import sys
sys.modules[__name__] = Benchmarks