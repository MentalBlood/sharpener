from functools import partial
from rich.table import Table
from rich.console import Console



class Reports(dict):

	def __init__(
		self, 
		*args,
		processTime=lambda n: '{:f}'.format(round(n, ndigits=8)),
		sort_by='time',
		is_sort_reversed=True,
	):

		self.processTime = processTime
		self.sort_by = sort_by
		self.is_sort_reversed=is_sort_reversed
	
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
				'',
				str(self.processTime(data['time']))
			)

			functions = list(data['calls'].items())

			if self.sort_by in ['number', 'time']:
				functions.sort(key=lambda i: i[1][self.sort_by])
			else:
				functions.sort(key=lambda i: i[0])
			
			if self.is_sort_reversed:
				functions.reverse()
			
			for name, info in functions:
				table.add_row(
					'', 
					name, 
					str(info['number']),
					str(self.processTime(info['time'])),
				)
			
			table.rows[-1].end_section = True
		
		console = Console()
		with console.capture() as capture:
			console.print(table)
		str_output = capture.get()
		
		return str_output



import sys
sys.modules[__name__] = Reports