"""Точка входа: по очереди запускает run() каждого модуля-задания из пакета tasks."""
from importlib import import_module

# Имена начинаются с цифр, поэтому обычный import невозможен - только import_module.
TASK_MODULES = [
    '00_distance',
    '01_circle',
    '02_operations',
    '03_favorite_movies',
    '04_my_family',
    '05_zoo',
    '06_songs_list',
    '07_secret',
    '08_garden',
    '09_shopping',
    '10_store',
]


def run_all():
    for name in TASK_MODULES:
        import_module(f'tasks.{name}').run()
        print()


if __name__ == '__main__':
    run_all()
