# # За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m 
# # километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами. 
# n = int(input('Введите количество км в день, кот проезжает авто '))
# m = int(input('Введите длину маршрута '))
# res = m // -n
# print(f'Количество дней = {-res}')

# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для 
# них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в 
# каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.

# a = int(input('Количество учеников первого класса '))
# b = int(input('Количество учеников второго класса '))
# c = int(input('Количество учеников третьего класса '))
# result  = (a + b + c) // -2
# print(abs(result))

# Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны 
# нумеруются от «головы» поезда, а иногда – с «хвоста»; это зависит от того, в какую сторону едет 
# электричка). В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил, 
# что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке. Напишите 
# программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.
# i = 3
# j = 4
# if i == j:
# print("Данных не хватает")
# else:
# print(i+j-1)

# Дано натуральное число. Требуется определить, является ли год с данным номером високосным. Если 
# год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с 
# григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.
# a = int(input('Введите год '))
# if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
#     print('YES')
# else:
#     print('NO')    

# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала
# в два раза больше журавликов, чем Петя и Сережа вместе?
# Выведите кортеж из количества журавликов, сделанных Петей, Катей и Сережей.

# n = int(input())
# k = int((n/3)*2)
# p = int((k/2)/2)
# s = int(p)
# print(p, k, s)

# Вы пользуетесь общественным транспортом? Вероятно, вырасплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где суммапервых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написатьпрограмму, которая проверяет счастливость билета.

# n1 = n // 100000
# n2 = (n % 100000) // 10000
# n3 = (n % 10000) // 1000
# n4 = (n % 1000) // 100
# n5 = (n % 100) // 10
# n6 = n % 10


# n = int(input())

# a = (n // 100000) + ((n % 100000) // 10000) + ((n % 10000) // 1000) 
# b = ((n % 1000) // 100) + ((n % 100) // 10) + (n % 10)
# if a == b:
#     print('yes')
# else:
#     print('no')


n = (input())
s1 = int(n[0]) + int(n[1]) + int(n[2])
s2 = int(n[3]) + int(n[4]) + int(n[5])
if s1 == s2:
    print('YES')
else:
    print('NO')

    

# Требуется определить, можно ли от шоколадки размером a × b долек отломить c долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на двапрямоугольника).
    
# a = int(input())
# b = int(input())
# c = int(input())    
# if c < a * b and (c % b == 0 or c % a == 0):
#     print('yes')
# else:
#     print('no')
