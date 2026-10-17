#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

MOVIES_LINE = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться. Переопределять my_favorite_movies нельзя.
# Использовать .split() или .find() или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!


def pick_movies(line):
    return (
        line[:10],
        line[-15:],
        line[12:25],
        line[-22:-17],
    )


def run():
    for title in pick_movies(MOVIES_LINE):
        print(title)

def all_movies(line):
    return (
        line[:10],       # Терминатор
        line[12:25],     # Пятый элемент
        line[27:33],     # Аватар
        line[-22:-17],     # Чужие
        line[-15:],       # Назад в будущее
    )


def run_filters():
    first_list = pick_movies(MOVIES_LINE)

    print('Первый список в обр порядке:')
    for title in first_list[::-1]:
        print(title)

    print('От самого корот. к самому длинн.')
    for title in sorted(all_movies(MOVIES_LINE), key=len):
        print(title)


if __name__ == '__main__':
    run()
    run_filters()