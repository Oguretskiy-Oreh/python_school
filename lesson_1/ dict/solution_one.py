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


dict_of_players = {'Jack': 69485, 'Michail': 95715, 'Alex': 95715, 'Morgan': 83647, 'Jerry': 197128, 'Nikole': 95715, 'Lauren': 93289}
for i, j in dict_of_players.items():
	if j == max(dict_of_players.values()):
		print(i, j)
