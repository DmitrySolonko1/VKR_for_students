import django_filters
from .models import *


class RentalFilter(django_filters.FilterSet):
    SIMPLE_CHOICE = (
        ('Да', 'Да'),
        ('Нет', 'Нет')
    )

    CHOICE_CITY = (
        ('Казань', 'Казань'),
    )

    CHOICE_DISTRICT = (
        ('', 'Любой'),
        ('Советский', 'Советский'),
        ('Приволжский', 'Приволжский'),
        ('Вахитовский', 'Вахитовский'),
        ('Московский', 'Московский'),
        ('Авиастроительный', 'Авиастроительный'),
        ('Ново - Савиновский', 'Ново - Савиновский'),
    )
    CHOICE_FINISHING = (
        ('', 'Любой'),
        ('Без отделки', 'Без отделки'),
        ('под чистовую отделку', 'под чистовую отделку'),
        ('Косметический', 'Косметический'),
        ('Капитальный', 'Капитальный'),
        ('евроремонт', 'евроремонт'),
        ('ремонт премиум-класса', 'ремонт премиум-класса'),
    )
    CHOICE_TYPE = (
        ('', 'Любой'),
        ('Новостройка', 'Новостройка'),
        ('Вторичка', 'Вторичка'),
    )
    CHOICE_LAYOUT = (
        ('', 'Любая'),
        ('Смежная', 'Смежная'),
        ('Изолированная', 'Изолированная'),
        ('Улучшенная', 'Улучшенная'),
        ('Свободная', 'Свободная'),
        ('Студия', 'Студия'),
        ('Евро', 'Евро'),
        ('2-уровневая', '2-уровневая')
    )
    CHOICE_BATHROOM = (
        ('', 'Любой'),
        ('совмещенный', 'совмещенный'),
        ('раздельный', 'раздельный'),
    )
    CHOICE_BALCONY = (
        ('', 'Неважно'),
        ('Балкон', 'Балкон'),
        ('Лоджия', 'Лоджия'),
        ('Отсутствует', 'Отсутствует')
    )
    CHOICE_STATUS = (
        ('В работе', 'В работе'),
        ('Приостановлено', 'Приостановлено'),
        ('Закончено', 'Закончено'),
    )
    CHILDREN_ANIMALS_STATUS = (
        ('', 'Неважно'),
        (True, "Можно"),
        (False, "Нельзя"),
    )

    CHOICE_ROOMS = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    )
    district = django_filters.MultipleChoiceFilter(choices=CHOICE_DISTRICT, lookup_expr="icontains")
    price = django_filters.RangeFilter(label='Цена')
    area = django_filters.RangeFilter(label='Площадь кв.м')
    floor = django_filters.RangeFilter(label='Этаж')
    rooms = django_filters.MultipleChoiceFilter(choices=CHOICE_ROOMS, lookup_expr="icontains")
    type = django_filters.MultipleChoiceFilter(choices=CHOICE_TYPE, lookup_expr="icontains")
    layout = django_filters.MultipleChoiceFilter(choices=CHOICE_LAYOUT, lookup_expr="icontains")
    finishing = django_filters.MultipleChoiceFilter(choices=CHOICE_FINISHING, lookup_expr="icontains")
    bathroom = django_filters.MultipleChoiceFilter(choices=CHOICE_BATHROOM, lookup_expr="icontains")
    balcony = django_filters.MultipleChoiceFilter(choices=CHOICE_BALCONY, lookup_expr="icontains")
    animals = django_filters.MultipleChoiceFilter(choices=CHILDREN_ANIMALS_STATUS, lookup_expr="icontains")
    children = django_filters.MultipleChoiceFilter(choices=CHILDREN_ANIMALS_STATUS, lookup_expr="icontains")
    parking = django_filters.MultipleChoiceFilter(choices=SIMPLE_CHOICE, lookup_expr="icontains")

    class Meta:
        model = RealEstate
        fields = ['district', 'price', 'area', 'floor', 'rooms', 'type', 'layout', 'finishing', 'bathroom', 'balcony',
                  'animals', 'children', 'parking']
