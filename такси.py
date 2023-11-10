from num2words import num2words
# Сортировка слиянием по убывание
def merge_sort_decrease(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort_decrease(left)
        merge_sort_decrease(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
# Сортировка слиянием по возрастанию
def merge_sort_increase(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort_increase(left)
        merge_sort_increase(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

n = 0
while n <= 0:
    flag = 0
    # что бы проверить является ли введенная строка числом попробуем преобразовать ее в int и будем ловить исключение
    try:
        n = int(input('Введите количество сотрудников в компании: '))
    except ValueError:
        print("\033[31m", "Количество сотрудников должно быть задано числом !!!" + '\033[0m')
        flag = 1
        pass
    # Проверяем, что введенное число положительное
    if n <= 0 and flag == 0:
        print("\033[31m", "Количество сотрудников должно быть задано положительным числом !!!" + '\033[0m')

array_km = []  # массив: расстоянием до дома + номер сотрудника
print('\033[1m' + 'Введите поочередно расстояние до дома: ' + '\033[0m')
for i in range(1, n + 1):
    km = 0
    while km <= 0:
        flag = 0
        # что бы проверить является ли введенная строка числом попробуем преобразовать ее в int и будем ловить исключение
        try:
            km = int(input(f'{i} сотрудника: '))
        except ValueError:
            print("\033[31m", "Расстояние до дома должно быть задано числом !!!" + '\033[0m')
            flag = 1
            pass
        # Проверяем, что введенное число положительное
        if km <= 0 and flag == 0:
            print("\033[31m", "Расстояние до дома должно быть задано положительным числом !!!" + '\033[0m')
    array_km.append([km + i / 10 ** len(str(i))])
# сортируем сотрудников по расстоянию до дома(по возрастанию)
merge_sort_increase(array_km)

#  массив: номер машины, тариф
array_cost = []
print('\033[1m' + 'Введите поочередно стоимость в рублях за проезд одного километра: ' + '\033[0m')
for i in range(1, n + 1):
    rate = 0
    while rate <= 0:
        flag = 0
        # что бы проверить является ли введенная строка числом попробуем преобразовать ее в int и будем ловить исключение
        try:
            rate = int(input(f'в {i} машине такси: '))
        except ValueError:
            print("\033[31m", "Стоимость должно быть задано числом !!!" + '\033[0m')
            flag = 1
            pass
        # Проверяем, что введенное число положительное
        if rate <= 0 and flag == 0:
            print("\033[31m", "Стоимость должно быть задано положительным числом !!!" + '\033[0m')
    array_cost.append([rate + i / 10 ** len(str(i))])
# сортируем такси по тарифу в рублях(по убыванию)
merge_sort_decrease(array_cost)

#  массив: номер сотрудника, номер такси, стоимость поездки
array_ride = []
for i in range(0, n):
    array_km_split = str(array_km[i][0]).split('.')
    array_cost_split = str(array_cost[i][0]).split('.')
    array_ride.append([array_km_split[1] + '.' + array_cost_split[1] + '.' + str(int(array_km_split[0]) * int(array_cost_split[0]))])
#  сортируем сотрудников по их номеру (по возрастанию)
merge_sort_increase(array_ride)

print('\033[1m' + 'Оптимальный вариант рассадки сотрудников: ' + '\033[0m')
for i in range(0, n):
    array_ride_split = array_ride[i][0].split('.')
    print(f'{array_ride_split[1]} такси для {i + 1} сотрудника, ', end='')

#  Рассчитываем общую стоимость поездки
cost = 0
for i in range(0, n):
    array_ride_split = array_ride[i][0].split('.')
    cost += int(array_ride_split[2])
print('\033[1m' + '\n\nОбщая стоимость поездок составит: ' + '\033[0m' + f'{cost} рубля')

# Преобразуем число в слова с помощью num2words
summa_words = num2words(cost, lang='ru')

# Определяем правильное окончание для рублей
if cost % 10 == 1 and cost != 11:
    currency = "рубль"
elif cost % 10 in [2, 3, 4] and (cost % 100 < 10 or cost % 100 > 20):
    currency = "рубля"
else:
    currency = "рублей"

# Выводим результат
print('\033[1m' + 'Общая стоимость поездок составит: ' + '\033[0m' + f"{summa_words.capitalize()} {currency}")
