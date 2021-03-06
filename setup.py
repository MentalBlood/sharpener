import os
from setuptools import setup, find_packages



if __name__ == '__main__':

	long_description = ''
	if os.path.exists('README.md'):
		with open('README.md', encoding='utf-8') as f:
			long_description = f.read()

	setup(
		name='sharpener',
		version='1.0.0',
		description='Handy profiling/benchmarking tool',
		long_description=long_description,
		long_description_content_type='text/markdown',
		author='mentalblood',
		install_requires=[
			'rich',
			'tqdm'
		],
		packages=find_packages()
	)
