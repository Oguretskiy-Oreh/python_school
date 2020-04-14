# 1. Есть данные с компьютерной игры:
# 69485 Jack
# 95715 Michail
# 95715 Alex
# 83647 Morgan
# 197128 Jerry
# 95715 Nikole
# 93289 Lauren
# где можно найти очки, которые заработал пользователь.
# Нужно создать словарь из этих данных, найти победителя.

dict_of_players = {'Джек': 69485, 'Михаил': 95715, 'Алекс': 95715, 'Морган': 83647, 'Джерри': 197128, 'Николь': 95715, 'Лорен': 93289}
values = []
for value in dict_of_players.values():
	values.append(int(value))
	values.sort()
for winner, value in dict_of_players.items():
	if value == values[-1]:
		print(winner, value)
