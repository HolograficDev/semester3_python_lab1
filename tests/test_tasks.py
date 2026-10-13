from importlib import import_module

import pytest

def _task(name):
    return import_module(f'tasks.{name}')


city_distances = _task('00_distance')
circle_geometry = _task('01_circle')
expression_puzzle = _task('02_operations')
movie_slices = _task('03_favorite_movies')
family_heights = _task('04_my_family')
zoo_cages = _task('05_zoo')
track_durations = _task('06_songs_list')
cipher_decoder = _task('07_secret')
flower_sets = _task('08_garden')
candy_prices = _task('09_shopping')
warehouse_stock = _task('10_store')


def test_distance_table_is_symmetric_and_has_no_self_pairs():
    table = city_distances.build_distance_table(city_distances.CITY_COORDS)
    assert 'Paris' not in table['Paris']
    assert table['London']['Paris'] == pytest.approx(42.4264, abs=1e-4)
    assert table['Moscow']['London'] == table['London']['Moscow']


def test_circle_area_and_points():
    assert circle_geometry.circle_area(42) == 5541.7693
    assert circle_geometry.is_inside_circle((23, 34), 42) is True
    assert circle_geometry.is_inside_circle((30, 30), 42) is False
    assert circle_geometry.is_inside_circle((42, 0), 42) is False  # граница не считается внутри


def test_expression_equals_25():
    assert expression_puzzle.make_twenty_five() == 25


def test_movie_slices():
    assert movie_slices.pick_movies(movie_slices.MOVIES_LINE) == (
        'Терминатор', 'Назад в будущее', 'Пятый элемент', 'Чужие',
    )


def test_family_heights():
    assert family_heights.father_height(family_heights.HEIGHTS_CM) == 172
    assert family_heights.father_height([['я', 180]]) is None
    assert family_heights.total_height(family_heights.HEIGHTS_CM) == 522


def test_zoo_steps_and_immutability():
    original = list(zoo_cages.CAGES)
    with_bear = zoo_cages.seat_bear(zoo_cages.CAGES)
    assert with_bear[:3] == ['lion', 'bear', 'kangaroo']
    with_birds = zoo_cages.add_birds(with_bear, zoo_cages.BIRDS)
    final = zoo_cages.remove_animal(with_birds, 'elephant')
    assert final == ['lion', 'bear', 'kangaroo', 'monkey', 'rooster', 'ostrich', 'lark']
    assert zoo_cages.cage_number(final, 'lion') == 1
    assert zoo_cages.cage_number(final, 'lark') == 7
    assert zoo_cages.CAGES == original


def test_track_durations():
    assert track_durations.duration_from_list(
        track_durations.TRACKS_AS_LIST, ['Halo', 'Enjoy the Silence', 'Clean']) == 14.93
    assert track_durations.duration_from_dict(
        track_durations.TRACKS_AS_DICT,
        ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']) == 13.49


def test_cipher_decoder():
    assert cipher_decoder.decode(cipher_decoder.ENCRYPTED_LINES) == 'в бане веник дороже денег'


def test_flower_sets():
    everything, shared, garden_only, meadow_only = flower_sets.compare_flowers(
        flower_sets.GARDEN_SET, flower_sets.MEADOW_SET)
    assert shared == {'ромашка', 'одуванчик'}
    assert garden_only == {'роза', 'гладиолус', 'подсолнух'}
    assert meadow_only == {'клевер', 'мак'}
    assert everything == shared | garden_only | meadow_only


def test_hardcoded_cheapest_offers_match_shops():
    for product, offers in candy_prices.CHEAPEST_OFFERS.items():
        all_prices = sorted(
            (item['price'], shop)
            for shop, items in candy_prices.SHOPS.items()
            for item in items if item['name'] == product
        )[:2]
        assert [(o['price'], o['shop']) for o in offers] == all_prices


def test_warehouse_stock():
    report = warehouse_stock.summarize_stock(warehouse_stock.PRODUCT_CODES, warehouse_stock.STOCK)
    assert report[0] == ('Лампа', 27, 1134)
    assert dict((p, c) for p, _, c in report) == {
        'Лампа': 1134, 'Стол': 27860, 'Диван': 3550, 'Стул': 10311,
    }
