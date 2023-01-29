import re

# [x] "Чернобыль (1)" (name)
# [x] "5" (episodes_count)
# [x] "1" (season)
# [x] "2019" (season_year)
# [x] "5" (season_episodes)
# [x] "1" (episode_number)
# [x] "1:23:45" (episode_name)
# [x] "1:23:45" (episode_original_name)
# [x] "6 мая 2019" (episode_date)

# Final regex:
# (?P<name>(?<=/\">).*(?=</a></h1></td>))|(?P<episodes_count>(?<=<td class=\"news\">)\d+(?=</td>))|(?P<season>(?<=Сезон )\d+(?=</h1>))|(?P<season_year>\d+(?=,\s+эпизодов:\s+\d+))|(?P<season_episodes>(?<=эпизодов:\s)\d+(?=\s*))|(?P<episode_number>(?<=Эпизод\s)\d+)|(?P<episode_name>(?<=<b>).+(?=<[/]b></h1>))|(?P<episode_original_name>(?<=episodesOriginalName\">).+(?=<[/]span>))|(?P<episode_date>(?<=\">)\d+\s+\w+\s\d{4}(?=<[/]td>))

f = open("task4/1309707.html", "r")
html = f.read()

pattern_name = r'(?P<name>(?<=/\">).*(?=</a></h1></td>))'
episodes = r'(?P<episodes_count>(?<=<td class=\"news\">)\d+(?=</td>))'
season = r'(?P<season>(?<=Сезон )\d+(?=</h1>))'
season_year = r'(?P<season_year>\d+(?=,\s+эпизодов:\s+\d+))'
season_episodes = r'(?P<season_episodes>(?<=эпизодов:\s)\d+(?=\s*))'
episode_number = r'(?P<episode_number>(?<=Эпизод\s)\d+)'
episode_name = r'(?P<episode_name>(?<=<b>).+(?=<[/]b></h1>))' # moviename-big
episode_original_name = r'(?P<episode_original_name>(?<=episodesOriginalName\">).+(?=<[/]span>))'  # episodesOriginalName
episode_date = r'(?P<episode_date>(?<=\">)\d+\s+\w+\s\d{4}(?=<[/]td>))'

patterns = pattern_name \
           + '|' + episodes \
           + '|' + season \
           + '|' + season_year \
           + '|' + season_episodes \
           + '|' + episode_number \
           + '|' + episode_name \
           + '|' + episode_original_name \
           + '|' + episode_date

regexp = re.compile(patterns)

print(regexp.pattern)

entities = set()
for match in regexp.finditer(html):
    for key, value in match.groupdict().items():
        if value is not None:
            start, end = match.span(key)
            print('(' + key + ')', '"' + html[start: end] + '"')
    entities.add((start, end, key))

# Assertions

test_episode_date = '<td align="left" class="news" style="border-bottom:1px dotted #ccc;padding:15px 0px;font-size:12px" valign="bottom" width="20%">14 августа 2020</td>'
answer_episode_date = '14 августа 2020'
assert regexp.search(test_episode_date).group() == answer_episode_date

test_moviename_big = '''<h1 class="moviename-big" style="font-size:16px;padding:0px;color:#444"><b>Trent Crimm: The Independent</b></h1>'''
answer_moviename_big = 'Trent Crimm: The Independent'
assert regexp.search(test_moviename_big).group() == answer_moviename_big
