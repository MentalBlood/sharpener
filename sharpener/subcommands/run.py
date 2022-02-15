import json
import glob

from .. import Benchmarks



description = 'Run benchmarks'

args = [
	('names',						'type',		'required',		'help',																'default'),
	(['-r', '--root'],				str,		False,			'Root folder path',													'.'),
	(['-cp', '--config_prefix'],	str,		False,			'Config file name prefix',											'benchmark_'),
	(['-c', '--config'],			str,		False,			'Config name (file name is "<config prefix>_<config name>.json")',	'default'),
	(['-p', '--profile'],			int,		False,			'Profile or not',													1)
]


def handler(args):

	config = None
	config_path_pattern = f'{args.root}/**/{args.config_prefix}{args.config}*.json'

	for file_path in glob.iglob(config_path_pattern, recursive=True):
		with open(file_path, 'rb') as f:
			config = json.load(f)
			break
	
	if not config:
		print(f'No config file found matching pattern "{config_path_pattern}"')
		exit(1)
	
	b = Benchmarks(args.root)

	reports = b.run(config, profile=bool(args.profile))

	print(reports)