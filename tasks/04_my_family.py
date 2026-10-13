#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
FAMILY = ['я', 'мама', 'папа']

# список списков приблизительного роста членов вашей семьи
HEIGHTS_CM = [
    ['я', 180],
    ['мама', 170],
    ['папа', 172],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см


def father_height(heights):
    """Рост «папы» или None, если его нет в списке."""
    return next((cm for name, cm in heights if name == 'папа'), None)


# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см


def total_height(heights):
    return sum(cm for _, cm in heights)


def run():
    print(f'Рост отца - {father_height(HEIGHTS_CM)} см')
    print(f'Общий рост моей семьи - {total_height(HEIGHTS_CM)} см')


if __name__ == '__main__':
    run()
