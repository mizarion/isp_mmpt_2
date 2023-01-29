import re

import regexp


pattern_name = r'(?P<name>^(.*?(\bpass\b)[^$]*)$)'

patterns = pattern_name
regexp = re.compile(patterns)


text = 'adasdsb pass asdasd'

entities = set()
for match in regexp.finditer(text):
    for key, value in match.groupdict().items():
        if value is not None:
            start, end = match.span(key)
    entities.add((start, end, key))



print(regexp.findall(text))
print(entities)
# Assertions
