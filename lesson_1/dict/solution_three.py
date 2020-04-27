# 3. Дан список стран и городов каждой страны. Затем даны названия городов.
# Russia: Moscow Petersburg Novgorod Kaluga
# Ukraine: Kiev Donetsk Odessa
#
# Для каждого города укажите, в какой стране он находится.
# Odessa
# Moscow
# Novgorod
# San Francisco


country = {'Russia': ['Moscow', 'Petersburg', 'Novgorod', 'Kaluga​'], 'Ukraine': ['Kiev', 'Donetsk', 'Odessa'], 'USA': ['San Francisco']}
city = ['Odessa', 'Moscow', 'Novgorod', 'San Francisco']
for co, ci in country.items():
	for c in ci:
		if c in city:
			print(c, '-', co)
