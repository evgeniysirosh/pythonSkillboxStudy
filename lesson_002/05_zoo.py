#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

print('После посадки медведя:')
print (zoo)

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль


# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark']
zoo.extend (birds)
print('После добавления птиц:')
print (zoo)
#  и выведите список на консоль
#

# уберите слона
#  и выведите список на консоль

zoo.remove('elephant')
print('После удаления слона:')
print(zoo)

print ('Номер клітки лева :',zoo.index('lion')+1)
print ('Номер клітки жаворонка:',zoo.index('lark')+1)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.

