#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

PRODUCT_CODES = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.
# Каждый товар может лежать в нескольких местах (партиях) с разной ценой.

STOCK = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# и вывести в формате
#   <товар> - <кол-во> шт, стоимость <сумма> руб

# Пример:
#   Лампа - 27 шт, стоимость 1134 руб


def summarize_stock(codes, stock):
    """Список (товар, общее количество, общая стоимость) в порядке словаря codes"""
    report = []
    for product, code in codes.items():
        lots = stock[code]
        report.append((
            product,
            sum(lot['quantity'] for lot in lots),
            sum(lot['quantity'] * lot['price'] for lot in lots),
        ))
    return report


def run():
    for product, qty, cost in summarize_stock(PRODUCT_CODES, STOCK):
        print(f'{product} - {qty} шт, стоимость {cost} руб')


if __name__ == '__main__':
    run()
