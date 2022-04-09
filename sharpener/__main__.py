import os
import glob
import json
import argparse

from . import Benchmarks



parser = argparse.ArgumentParser(description='Download audio from Bandcamp')
parser.add_argument(
	'-r',
	'--root',
	type=str,
	help='Root folder path',
	default='.',
	required=False
)
parser.add_argument(
	'-cp',
	'--config_prefix',
	type=str,
	help='Config file name prefix',
	default='benchmark_',
	required=False
)
parser.add_argument(
	'-c',
	'--config',
	type=str,
	help='Config name (file name is "<config prefix>_<config name>.json")',
	default='default',
	required=False
)
parser.add_argument(
	'-p',
	'--profile',
	type=int,
	help='Profile or not',
	default=1,
	required=False
)
args = parser.parse_args()


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