# В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло
# различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

# Input: 1 3 2 1 1 6
# Output: 10

sequence_bushes = tuple(map(int, input().split()))
AMOUNT_BUSHES = 3

max_sum = sequence_bushes[0]
for i in range(len(sequence_bushes)):
    if len(sequence_bushes) > 3:
        if max_sum < sum(sequence_bushes[i-j] 
                         for j in reversed(range(AMOUNT_BUSHES))):
            max_sum = sum(sequence_bushes[i-j]
                          for j in reversed(range(AMOUNT_BUSHES)))
    else:
        max_sum = sum(sequence_bushes)
print(f'Regular solution: {max_sum}')

print(f'Pro solution: ', end=' ')
print(max(
    (sum(sequence_bushes[i-j] for j in reversed(range(AMOUNT_BUSHES))) 
     if len(sequence_bushes) > 3 else sum(sequence_bushes)) 
     for i in range(len(sequence_bushes))))
