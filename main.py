# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

# n = int(input("ведите количество монеток"))
# i = 1
# heads = 0
# tails = 0
# while i <= n:
#     coin = int(input("какой стараной лежит монета(герб- 0, остальное решка"))
#     if coin == 0: heads += 1
#     else: tails += 1
#     i += 1
# if heads > tails:
#     print(f"нужно повернуть {tails}")
# else:print(f"нужно повернуть{heads}")

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
#  Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные  Петей числа.

# s = int(input("ведите сумму:"))
# p = int(input("ведите произведение:"))
# for x in range(s):
#     for y in range(p):
#         if s == x + y and p == x * y:
# print(f"задуманые число-{x} and {y}")

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input())
i = 0
while 2 ** i <= n:
    print(2 ** i)
i += 1