# 2. У нас есть оценки за некоторый промежуток времени у школьников:
# Мария: русский - 4, 3, 4; математика - 5, 4, 4; физика - 5, 5, 4;
# Павел: русский - 3, 3, 3; математика - 3, 4, 5, 3; физика - 5, 3, 4;
# Алексей: русский - 4, 5, 5, 5; математика - 5, 5, 4; физика - 5, 5, 4, 5;
# Ксения: русский - 4, 4, 4; математика - 3, 4, 4, 3; физика - 4, 4, 4;
# Нужно создать словарь из этих данных, вычислить средние оценки по предметам для каждого ученика.
# Добавить нового ученика: Дарья: русский - 4, математика - 5, физика - 3, 4.
# Найти всех учеников, у кого средняя оценка по математике выше 4.5.


guys_and_theme = {'Mariya': [['russkiy', 4, 3, 4], ['math', 5, 4, 4], ['physics', 5, 5, 5]], 'Pavel': [['russkiy', 3, 3, 3], ['math', 3, 4, 5], ['physics', 5, 3, 4]], 'Alexey': [['russkiy', 4, 5, 5, 5],  ['math', 5, 5, 4], ['phiysics', 5, 5, 4, 5]], 'Kseniya': [['russkiy', 4, 4, 4], ['math', 3, 4, 4, 3], ['physics', 4, 4, 4]]}
g = 0
c = 0
b = 0
t = []
v = []
for theme_marks in guys_and_theme.values():
	for i in theme_marks:
		for h in i[1:]:
			c += 1
			g += h
		i = [i[0], g / c]
		t.append(i)
		if len(t) == 3:
			v.append(t)
			t = []
		c = 0
		g = 0
for name in guys_and_theme.keys():
	guys_and_theme[name] = v[b]
	b += 1
guys_and_theme.update({'Daria': [['russkiy', 4], ['math', 5], ['physics', 3, 4]]})
for i, j in guys_and_theme.items():
	if j[1][1] > 4.5:
		print(i)
print(guys_and_theme)
