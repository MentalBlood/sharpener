import os
import glob
import importlib



class Benchmarks:

	def __init__(self, path='.', prefix='benchmark_'):
		
		self.path = path
		self.prefix = prefix
		self._modules = {}

		self.scan()
	
	@property
	def modules(self):
		return self._modules
	
	def scan(self):

		self._modules = {}
		
		for file_path in glob.iglob(f'{self.path}/**/{self.prefix}*.py', recursive=True):

			file_name = os.path.basename(file_path)
			without_ext = os.path.splitext(file_name)[0]
			module_name = without_ext[len(self.prefix):]
			
			spec = importlib.util.spec_from_file_location(module_name, file_path)
			module = importlib.util.module_from_spec(spec)
			spec.loader.exec_module(module)
			
			self._modules[module.__name__] = module



import sys
sys.modules[__name__] = Benchmarks