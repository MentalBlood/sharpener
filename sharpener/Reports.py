from rich.table import Table
from rich.console import Console



class Reports(dict):

	def __repr__(self):
		return super().__repr__()



import sys
sys.modules[__name__] = Reports