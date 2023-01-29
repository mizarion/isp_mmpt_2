import re

# в конце дубль ловящий последние предложения без точек
# []+[.]|[]+
pattern_simple_sentence = r'(?P<sentence>\b[\w\s,\"]+\.|\b[\w\s,\"]+$)'

# pattern_simple_sentence = r'\b[^.!?]+[.!?]+'
# pattern_multy = r'[\wА-Яа-я\s,\"]+[:](\s+\d+[.][\s\w;,]+)+\.'
# pattern_multy=    r'(\d+[.\s]+[\wА-Яа-я\s,\"]+[;])+'

pattern = pattern_simple_sentence
# pattern = pattern_multy
solver = re.compile(pattern)

f = open("text2_1.txt", "r")
text = f.read()  # .replace('\n', ' ')

# res = solver.search(text).groups()
# print(res)

print('pattern=', solver.pattern)

result = solver.findall(text)
for i in result:
    print('-' * 50)
    print(i)
    # str = ''+i
    # print(str.strip())

# Assertions

assert_text_1 = '''Что сразу бросается в глаза, так это нестандартная рисовка и отсутствие эмоций на лицах,
в первом сезоне "смешные" моменты были со вставками глупых лиц, как в аниме начала
2000х'''
assert_text_2 = 'Потом, видимо, поняли, что это уже не круто и от таких ходов отказались.'

assert_text_3 = '''Если не
обращать внимание на картинку, а полностью окунуться в сюжет, в принципе очень даже
смотрибельно.'''

assert_text_4 = '''Интересно следить за развитием персонажа, как он сначала вершит
правосудие над обидчиками своего отца, а потом глубоко погружается в овладение магией
разного толка.'''

assert_text_5 = '7 из 10'

assert solver.search(assert_text_1).group() == assert_text_1
assert solver.search(assert_text_2).group() == assert_text_2
assert solver.search(assert_text_3).group() == assert_text_3
assert solver.search(assert_text_4).group() == assert_text_4
assert solver.search(assert_text_5).group() == assert_text_5
