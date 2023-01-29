import re

pattern = r'(\((?:([^\(\)]*)|(?:(?2)(?1)(?2))*)\))'
solver = re.compile(pattern)

assert solver.search('()').group() == '()'
