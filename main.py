# Дана строчка, представляющая собой набор чисел. И дано число от 1 до 19 (не включая). Определить, присутствуют ли в
# строчке 2 цифры, такие, что сумма их равна введенному Вами числу, если да, то выведи эти цифры и их индексы.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# someString = input('Введите число\n')
# number = int(input('Введите число от 1 до 19\n'))
# index = 0
# index1 = 0
# while index < len(someString):
#     num1 = int(someString[index])
#     while index1 < len(someString):
#         num2 = int(someString[index1])
#         if num1 + num2 == number:
#             print('Первая цифра и индекс',num1, index)
#             print('Вторая цифра и индекс',num2, index1)
#         index1 += 1
#     index += 1
#     index1 = 0
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Даны две строки. Эти строки между собой отличаются только одним символом. Вторая строка получена путём добавления
# случайного символа в случайную позицию в первой строке. Вывести данный символ и его индекс.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
someString = str(input('Введите первое слово\n'))
someString1 = str(input('Введите второе слово\n'))
someString2 = someString
someString3 = someString1
index = 0
letter1 = ''
count = 0
if len(someString) + 1 == len(someString1):
    while index < len(someString):
        if someString[index] == someString1[index]:
            someString2 = someString2.replace(someString[index], '')
            someString3 = someString3.replace(someString1[index], '')
        else:
            letter1 = " " + someString1[index]
        index += 1
elif len(someString1) == len(someString1) + 1:
    while index < len(someString1):
        if someString[index] == someString1[index]:
            someString2 = someString2.replace(someString[index], '')
            someString3 = someString3.replace(someString1[index], '')
        else:
            letter1 = " " + someString[index]
        index += 1
else:
    print('Слова отличаются не на одну букву')
print(letter1)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~