# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит в строку первый список затем на следующией строке второй список.

text_1 = set(map(int, input().split()))
text_2 = set(map(int, input().split()))

print(*sorted((text_1.intersection(text_2))))