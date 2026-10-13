#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут

TRACKS_AS_LIST = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# Распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Обратите внимание, что суммирование чисел с плавающей точкой может давать погрешность,
# округлите результат до 3 знаков после запятой


def duration_from_list(tracks, titles):
    return round(sum(minutes for title, minutes in tracks if title in titles), 3)


# Есть словарь песен группы Depeche Mode
TRACKS_AS_DICT = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# Распечатайте общее время звучания трех других песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
# в формате
#   А другие три песни звучат ХХХ минут
# Обратите внимание на округление


def duration_from_dict(tracks, titles):
    return round(sum(tracks[title] for title in titles), 3)


def run():
    first = duration_from_list(TRACKS_AS_LIST, ['Halo', 'Enjoy the Silence', 'Clean'])
    print(f'Три песни звучат {first} минут')

    second = duration_from_dict(
        TRACKS_AS_DICT, ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']
    )
    print(f'А другие три песни звучат {second} минут')


if __name__ == '__main__':
    run()
