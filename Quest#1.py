# Монетки
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной
# и той же стороной.

from random import randint

coins = int(input('Сколько у вас монет: '))
randcoins = {}
coins0 = 0
coins1 = 0

for i in range(coins):
    randcoins[i] = randint(0, 1)
    if randcoins[i] < 1:
        coins0 = coins0 + 1
    else: 
        coins1 = coins1 + 1
# print(randcoins) #активировать для проверки

if coins0 <= coins1:
    print('Нужно перевернуть: ', coins0, 'монет')
elif coins1 <= coins0:
    print('Нужно перевернуть: ', coins1, 'монет')
