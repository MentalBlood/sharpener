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

		table.add_column('Benchmark')
		table.add_column('Function')
		table.add_column('Number', justify='right')
		table.add_column('Self time', justify='right')
		table.add_column('Time', justify='right')
		table.add_column('Percent', justify='right')

		for benchmark_name, data in self.items():
			
			table.add_row(
				benchmark_name,
				'',
				'',
				'',
				str(self.processTime(data['time'])),
				'100.0%'
			)

			functions = data['calls']
			
			for i, (name, info) in enumerate(functions):
				
				percentage = 100 * info['time'] / data['time']
				if percentage >= 70:
					color = 'red'
				elif percentage >= 40:
					color = 'bright_red'
				elif percentage >= 20:
					color='orange3'
				elif percentage >= 5:
					color = 'yellow'
				else:
					color = 'green'
				
				table.add_row(
					'', 
					name, 
					str(info['number']),
					str(self.processTime(info['self_time'])),
					str(self.processTime(info['time'])),
					f"{round(percentage, 1)}%",
					style=color
				)
			
			table.rows[-1].end_section = True
		
		console = Console()
		with console.capture() as capture:
			console.print(table)
		str_output = capture.get()
		
		return str_output



import sys
sys.modules[__name__] = Reports