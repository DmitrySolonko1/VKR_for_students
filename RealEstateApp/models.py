from django.db import models
from django.urls import reverse

from ProjectRealEstate import settings

SIMPLE_CHOICE = (
    ('Да', 'Да'),
    ('Нет', 'Нет')
)

CHOICE_CITY = (
    ('Казань', 'Казань'),
)

CHOICE_DISTRICT = (
    ('Советский', 'Советский'),
    ('Приволжский', 'Приволжский'),
    ('Вахитовский', 'Вахитовский'),
    ('Московский', 'Московский'),
    ('Авиастроительный', 'Авиастроительный'),
    ('Ново - Савиновский', 'Ново - Савиновский'),
)
CHOICE_FINISHING = (
    ('Без отделки', 'Без отделки'),
    ('под чистовую отделку', 'под чистовую отделку'),
    ('Косметический', 'Косметический'),
    ('Капитальный', 'Капитальный'),
    ('евроремонт', 'евроремонт'),
    ('дизайнерский', 'дизайнерский'),
    ('ремонт премиум-класса', 'ремонт премиум-класса'),
)
CHOICE_TYPE = (
    ('Новостройка', 'Новостройка'),
    ('Вторичка', 'Вторичка'),
)
CHOICE_LAYOUT = (
    ('Смежная', 'Смежная'),
    ('Изолированная', 'Изолированная'),
    ('Улучшенная', 'Улучшенная'),
    ('Свободная', 'Свободная'),
    ('Студия', 'Студия'),
    ('Евро', 'Евро'),
    ('2-уровневая', '2-уровневая')
)
CHOICE_BATHROOM = (
    ('совмещенный', 'совмещенный'),
    ('раздельный', 'раздельный'),
)
CHOICE_BALCONY = (
    ('Балкон', 'Балкон'),
    ('Лоджия', 'Лоджия'),
    ('Отсутствует', 'Отсутствует')
)
CHOICE_STATUS = (
    ('В работе', 'В работе'),
    ('Приостановлено', 'Приостановлено'),
    ('Закончено', 'Закончено'),
)


# Create your models here.
class RealEstate(models.Model):
    photo = models.ManyToManyField('Photo', blank=True)
    city = models.CharField(max_length=30, choices=CHOICE_CITY, verbose_name='Город')
    district = models.CharField(max_length=70, choices=CHOICE_DISTRICT, verbose_name='Район')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    latitude = models.FloatField(blank=True, null=True, verbose_name='Ширина')
    longitude = models.FloatField(blank=True, null=True, verbose_name='Долгота')
    area = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Площадь')
    floor = models.IntegerField(verbose_name='Этаж')
    rooms = models.IntegerField(verbose_name='Кол-во комнат')
    type = models.CharField(max_length=30, choices=CHOICE_TYPE, verbose_name='Тип недвижимости')
    layout = models.CharField(max_length=50, choices=CHOICE_LAYOUT, verbose_name='Планировка')
    finishing = models.CharField(max_length=70, choices=CHOICE_FINISHING, verbose_name='Ремонт')
    bathroom = models.CharField(max_length=30, choices=CHOICE_BATHROOM, verbose_name='Сан.узел')
    balcony = models.CharField(max_length=50, choices=CHOICE_BALCONY, verbose_name='Балкон/Лоджия')
    animals = models.BooleanField(default=False, verbose_name='С животными')
    children = models.BooleanField(default=True, verbose_name='С детьми')
    parking = models.CharField(max_length=200, choices=SIMPLE_CHOICE, blank=True, verbose_name='Парковка')
    description = models.TextField(verbose_name='Полное описание')
    price = models.DecimalField(max_digits=15, decimal_places=1, verbose_name='Стоимость')
    realtor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Риелтор',
                                limit_choices_to={'is_staff': True}, )
    category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name='Категория')
    status = models.CharField(max_length=50, choices=CHOICE_STATUS, verbose_name='Статус')

    def __str__(self):
        return "ID объекта: " + str(self.pk) + '; ' + str(self.district) + ", " + str(self.address)

    def get_absolute_url(self):
        return reverse("RealEstate_object", kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Объект недвижимости'
        verbose_name_plural = 'Объекты недвижимости'


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Photo(models.Model):
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'


class TimeSlot(models.Model):
    time = models.DateTimeField(verbose_name='Дата и время бронирования')
    is_available = models.BooleanField(default=True, verbose_name='Статус')

    def __str__(self):
        return str(self.time)

    class Meta:
        verbose_name = 'Время бронирования'
        verbose_name_plural = 'Время бронирования'


class Booking(models.Model):
    object = models.ForeignKey(RealEstate, on_delete=models.CASCADE, verbose_name='Объект для брони')
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, verbose_name='Время бронирования')
    client_name = models.CharField(max_length=255, verbose_name='Клиент')
    realtor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Риелтор',
                                limit_choices_to={'is_staff': True}, )

    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Бронь'


class Contracts(models.Model):
    object = models.ForeignKey(RealEstate, on_delete=models.CASCADE, verbose_name='Объект')
    client_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Клиент',
                                    limit_choices_to={'is_staff': False}, related_name='contract_client')
    realtor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Риелтор',
                                limit_choices_to={'is_staff': True}, related_name='contract_rieltor')
    price = models.DecimalField(max_digits=15, decimal_places=1, verbose_name='Стоимость')
    date = models.DateField(verbose_name='Дата')

    def __str__(self):
        return str(self.client_name)


    def save(self, *args, **kwargs):
        # Вычисление стоимости контракта как стоимость объекта + 20%
        self.price = float(self.object.price) * 1.2
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договора'
