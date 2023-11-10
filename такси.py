n = int(input('Введите количество сотрудникво в компании: '))
array_km = []  # массив: номер сотрудника, расстоянием до дома
print('\033[1m' + 'Введите поочередно растояние до дома: ' + '\033[0m')
for i in range(1, n + 1):
    km = int(input(f'{i} сотрубника: '))
    array_km.append([i, km])
# сортируем сотрудников по расстоянию до дома(по возрастанию)
array_km.sort(key=lambda x: x[1])

#  массив: номер машины, тариф
array_cost = []
print('\033[1m' + 'Введите поочередно стоимость в рублях за проезд одного километра:' + '\033[0m')
for i in range(1, n + 1):
    rate = int(input(f'в {i} машине такси: '))
    array_cost.append([i, rate])
# сортируем такси по тарифу в рублях(по убыванию)
array_cost.sort(key=lambda x: x[1], reverse=True)

#  массив: номер сотрудника, номер такси, стоимость поездки
array_ride = []
for i in range(0, n):
    array_ride.append([array_km[i][0], array_cost[i][0], array_km[i][1] * array_cost[i][1]])
#  сортируем сотрудников по их номеру
array_ride.sort(key=lambda x: x[0])

print('\033[1m' + 'Оптимальный вариант рассадки сотрудников: ' + '\033[0m')
for i in range(0, n):
    print(f'{array_ride[i][1]} такси для {i + 1} сотрудника, ', end='')

#  Рассчитываем общую стоимость поездки
cost = 0
for i in range(0, n):
    cost += array_ride[i][2]
print('\033[1m' + '\nОбщая стоимость поездок составит: ' + '\033[0m' + f'{cost} рубля')
