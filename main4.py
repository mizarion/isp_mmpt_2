import re

# [x] "Чернобыль (1)" (name)
# [x] "5" (episodes_count)
# [x] "1" (season)
# [x] "2019" (season_year)
# [x] "5" (season_episodes)
# [x] "1" (episode_number)
# [x] "1:23:45" (episode_name)
# [x] "1:23:45" (episode_original_name)
#  "6 мая 2019" (episode_date)
#  "2" (episode_number)
#  "Пожалуйста, сохраняйте спокойствие" (episode_name)
#  "Please Remain Calm" (episode_original_name)
#  "13 мая 2019" (episode_date)
#  "3" (episode_number)
#  "Да разверзнется земля!" (episode_name)
#  "Open Wide, O Earth" (episode_original_name)
#  "20 мая 2019" (episode_date)
#  "4" (episode_number)
#  "Счастье всего человечества" (episode_name)
#  "The Happiness of All Mankind" (episode_original_name)
#  "27 мая 2019" (episode_date)
#  "5" (episode_number)
#  "Вечная память" (episode_name)
#  "Vichnaya Pamyat" (episode_original_name)
#  "3 июня 2019" (episode_date)

f = open("task4/1309707.html", "r")
html = f.read()

pattern_name = r'(?P<name>(?<=/\">).*(?=</a></h1></td>))'
episodes = r'(?P<episodes_count>(?<=<td class=\"news\">)\d+(?=</td>))'
season = r'(?P<season>(?<=Сезон )\d+(?=</h1>))'
season_year = r'(?P<season_year>\d+(?=,\s+эпизодов:\s+\d+))'
season_episodes = r'(?P<season_episodes>(?<=эпизодов:\s)\d+(?=\s*))'
episode_number = r'(?P<episode_number>(?<=Эпизод\s)\d+)'
episode_name = r'(?P<episode_name>(?<=<b>).+(?=<[/]b></h1>))' # moviename-big
episode_original_name = r'(?P<episode_original_name>(?<=episodesOriginalName\">).+(?=<[/]span>))' #episodesOriginalName

patterns = pattern_name \
           + '|' + episodes \
           + '|' + season \
           + '|' + season_year \
           + '|' + season_episodes \
           + '|' + episode_number \
           + '|' + episode_name \
           + '|' + episode_original_name

regexp = re.compile(patterns)

print(regexp.pattern)

entities = set()
for match in regexp.finditer(html):
    for key, value in match.groupdict().items():
        if value is not None:
            start, end = match.span(key)
            print('(' + key + ')', '"' + html[start: end] + '"')
    entities.add((start, end, key))

# print(regexp.findall(html))
# for i in regexp.findall(html):
#     print(i)

# print(entities, sep='\n')
# for entity in entities:
#     print(html[entity[0]:entity[1]], entity[2])

# Assertions
