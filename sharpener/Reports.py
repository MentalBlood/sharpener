from functools import partial
from rich.table import Table
from rich.console import Console



class Reports(dict):

	def __init__(
		self, 
		*args,
		processTime=lambda n: '{:f}'.format(round(n, ndigits=8))
	):
		self.processTime = processTime
		super().__init__(*args)

	def __str__(self):

		table = Table(show_header=True, header_style='bold')

		table.add_column('Benchmark', style='magenta')
		table.add_column('Function', style='blue')
		table.add_column('Number', justify='right')
		table.add_column('Time', style='white', justify='right')

		for benchmark_name, data in self.items():
			
			table.add_row(
				benchmark_name,
				'',
				str(sum([f['number'] for f in data['calls'].values()])), 
				str(self.processTime(sum([f['time'] for f in data['calls'].values()]))),
			)
			
			for function_name in data['calls']:
				table.add_row(
					'', 
					function_name, 
					str(data['calls'][function_name]['number']),
					str(self.processTime(data['calls'][function_name]['time'])),
				)
			
			table.rows[-1].end_section = True
		
		console = Console()
		with console.capture() as capture:
			console.print(table)
		str_output = capture.get()
		
		return str_output



import sys
sys.modules[__name__] = Reports