import re

import regexp

f = open("task4/77164.html", "r")
html = f.read()

pattern_name = r'(?P<name>(?<=/\">).*?[\s].*?(?=</a></h1></td>))'

patterns = pattern_name
regexp = re.compile(patterns)



entities = set()
for match in regexp.finditer(html):
    for key, value in match.groupdict().items():
        if value is not None:
            start, end = match.span(key)
    entities.add((start, end, key))



print(regexp.findall(html))
print(entities)
# Assertions
