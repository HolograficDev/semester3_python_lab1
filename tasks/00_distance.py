#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

CITY_COORDS = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def build_distance_table(coords):
    """{город: {другой_город: расстояние}}, пары город = он сам пропускаются"""
    table = {}
    for origin, (x0, y0) in coords.items():
        table[origin] = {
            target: ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
            for target, (x1, y1) in coords.items()
            if target != origin
        }
    return table


def run():
    print(build_distance_table(CITY_COORDS))


if __name__ == '__main__':
    run()
