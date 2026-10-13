#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В саду сорвали цветы
GARDEN_FLOWERS = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')

# На лугу сорвали цветы
MEADOW_FLOWERS = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')

# Создайте множество цветов, произрастающих в саду и на лугу
GARDEN_SET = set(GARDEN_FLOWERS)
MEADOW_SET = set(MEADOW_FLOWERS)

# Выведите на консоль все виды цветов
# Выведите на консоль те, которые растут и там и там
# Выведите на консоль те, которые растут в саду, но не растут на лугу
# Выведите на консоль те, которые растут на лугу, но не растут в саду


def compare_flowers(garden_set, meadow_set):
    """Возвращает (все, общие, только в саду, только на лугу)."""
    return (
        garden_set | meadow_set,
        garden_set & meadow_set,
        garden_set - meadow_set,
        meadow_set - garden_set,
    )


def run():
    everything, shared, garden_only, meadow_only = compare_flowers(GARDEN_SET, MEADOW_SET)
    print('Все виды:', everything)
    print('И там, и там:', shared)
    print('Только в саду:', garden_only)
    print('Только на лугу:', meadow_only)


if __name__ == '__main__':
    run()
