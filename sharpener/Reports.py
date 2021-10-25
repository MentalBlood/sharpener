from functools import partial
from rich.table import Table
from rich.console import Console



class Reports(dict):

	def __init__(
		self, 
		*args,
		processNumber=partial(round, ndigits=8)
	):
		self.processNumber = processNumber
		super().__init__(*args)

	def __str__(self):

		table = Table(show_header=True, header_style="bold magenta")

		table.add_column('Benchmark')
		table.add_column('Function')
		table.add_column('Number')
		table.add_column('Time')

		for benchmark_name, data in self.items():
			
			table.add_row(benchmark_name)
			
			for function_name in data['calls']:
				table.add_row(
					'', 
					function_name, 
					str(self.processNumber(data['calls'][function_name]['number'])),
					str(self.processNumber(data['calls'][function_name]['time']))
				)
			
			table.add_row(
				'', 
				'', 
				str(self.processNumber(sum([f['number'] for f in data['calls'].values()]))), 
				str(self.processNumber(sum([f['time'] for f in data['calls'].values()])))
			)
		
		console = Console()
		with console.capture() as capture:
			console.print(table)
		str_output = capture.get()
		
		return str_output



import sys
sys.modules[__name__] = Reports