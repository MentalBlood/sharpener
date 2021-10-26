import os
import glob
import importlib


from . import report, Reports, Benchmark



class Benchmarks:

	def __init__(self, path='.', file_prefix='benchmark_'):
		
		self.path = path
		self.file_prefix = file_prefix
		self._modules = {}

		self.scan()
	
	@property
	def modules(self):
		return self._modules
	
	def scan(self):

		self._modules = {}
		
		for file_path in glob.iglob(f'{self.path}/**/{self.file_prefix}*.py', recursive=True):

			file_name = os.path.basename(file_path)
			without_ext = os.path.splitext(file_name)[0]
			module_name = without_ext[len(self.file_prefix):]
			
			spec = importlib.util.spec_from_file_location(module_name, file_path)
			module = importlib.util.module_from_spec(spec)
			spec.loader.exec_module(module)

			module_dict = {}
			self._modules[module.__name__] = module_dict

			for name in dir(module):

				something = getattr(module, name)
				
				if hasattr(something, '__bases__') and Benchmark in something.__bases__:
					module_dict[name] = something
	
	def run(self, kwargs, exclude_calls=[]):

		reports = Reports()

		for name in kwargs:

			if not '::' in name:
				continue

			module_name, function_name = name.split('::')
			bench_class = self._modules[module_name][function_name]

			bench = bench_class(**kwargs[name])
			bench.prepare()

			reports[name] = report(bench.run, exclude_calls=exclude_calls)

			bench.clean()
		
		return reports



import sys
sys.modules[__name__] = Benchmarks