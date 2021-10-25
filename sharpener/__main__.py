from admiral import Parsers



p = Parsers(description='Handy profiling/benchmarking tool')
p.load('sharpener', ['run'])

result = p.run()