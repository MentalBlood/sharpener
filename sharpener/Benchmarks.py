import os
import glob
import importlib
from tqdm.auto import tqdm

from . import report, Reports, Benchmark, getMeanDict



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
	
	def run(self, config, exclude_calls=[], profile=True):

		reports = Reports()

		for name in tqdm(list(config.keys()), desc='Running benchmarks'):

			if not '::' in name:
				continue

			module_name, function_name = name.split('::')
			bench_class = self._modules[module_name][function_name]

			bench = bench_class(**{
				k: v
				for k, v in config[name].items()
				if not (k.startswith('__') and k.endswith('__'))
			})

			n = config[name]['__n__'] if '__n__' in config[name] else 1

			reports_to_mean = []
			for i in range(n):
				bench.prepare()
				reports_to_mean.append(report(bench.run, exclude_calls, profile))
				bench.clean()
			
			reports[name] = getMeanDict(*reports_to_mean)
		
		def getCallsFilter(name):

			if not '__calls__' in config[name]:
				return lambda x: True

			inclusions = config[name]['__calls__']
			
			def calls_filter(x):
				for i in inclusions:
					if i.lower() in x.lower():
						return True
				return False
			
			return calls_filter

		for name, r in reports.items():
			
			r['calls'] = [
				(k, v)
				for k, v in r['calls'].items()
				if getCallsFilter(name)(k)
			]
			r['calls'].sort(key=lambda i: i[1]['time'])
			r['calls'].reverse()

			if '__limit__' in config[name]:
				r['calls'] = r['calls'][:config[name]['__limit__']]
		
		return reports



import sys
sys.modules[__name__] = Benchmarks