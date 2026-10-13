#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список животных в зоопарке
CAGES = ['lion', 'kangaroo', 'elephant', 'monkey']

# Посадите медведя (bear) между львом и кенгуру
# и выведите список на консоль


def seat_bear(cages):
    """Возвращает новый список; медведь встаёт прямо перед кенгуру."""
    pos = cages.index('kangaroo')
    return cages[:pos] + ['bear'] + cages[pos:]


# Добавьте птиц из списка birds в последние клетки зоопарка
BIRDS = ['rooster', 'ostrich', 'lark']
# и выведите список на консоль


def add_birds(cages, birds):
    return cages + birds


# Уберите слона (elephant) из зоопарка
# и выведите список на консоль


def remove_animal(cages, animal):
    return [name for name in cages if name != animal]


# Выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть 1-индексированными (первая клетка - номер 1).


def cage_number(cages, animal):
    return cages.index(animal) + 1


def run():
    step = seat_bear(CAGES)
    print(step)
    step = add_birds(step, BIRDS)
    print(step)
    step = remove_animal(step, 'elephant')
    print(step)
    print(f'Лев в клетке №{cage_number(step, "lion")}')
    print(f'Жаворонок в клетке №{cage_number(step, "lark")}')


if __name__ == '__main__':
    run()
