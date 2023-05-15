# Generated by Django 4.1.7 on 2023-05-11 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(choices=[('Казань', 'Казань')], max_length=30, verbose_name='Город')),
                ('district', models.CharField(choices=[('Советский', 'Советский'), ('Приволжский', 'Приволжский'), ('Вахитовский', 'Вахитовский'), ('Московский', 'Московский'), ('Авиастроительный', 'Авиастроительный'), ('Ново - Савиновский', 'Ново - Савиновский')], max_length=70, verbose_name='Требуемый район')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('area', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Площадь')),
                ('floor', models.IntegerField(verbose_name='Этаж')),
                ('type', models.CharField(choices=[('Новостройка', 'Новостройка'), ('Вторичка', 'Вторичка')], max_length=30, verbose_name='Тип недвижимости')),
                ('layout', models.CharField(choices=[('Смежная', 'Смежная'), ('Изолированная', 'Изолированная'), ('Улучшенная', 'Улучшенная'), ('Свободная', 'Свободная'), ('Студия', 'Студия'), ('Евро', 'Евро'), ('2-уровневая', '2-уровневая')], max_length=50, verbose_name='Планировка')),
                ('finishing', models.CharField(choices=[('Без отделки', 'Без отделки'), ('под чистовую отделку', 'под чистовую отделку'), ('хорошее состояние', 'хорошее состояние'), ('евроремонт', 'евроремонт'), ('ремонт премиум-класса', 'ремонт премиум-класса')], max_length=70, verbose_name='Ремонт')),
                ('bathroom', models.CharField(choices=[('совмещенный', 'совмещенный'), ('раздельный', 'раздельный')], max_length=30, verbose_name='Сан.узел')),
                ('balcony', models.CharField(choices=[('Балкон', 'Балкон'), ('Лоджия', 'Лоджия'), ('Отсутствует', 'Отсутствует')], max_length=50, verbose_name='Балкон/Лоджия')),
                ('animals', models.BooleanField(default=False, verbose_name='С животными')),
                ('children', models.BooleanField(default=True, verbose_name='С детьми')),
                ('parking', models.CharField(blank=True, choices=[('Да', 'Да'), ('Нет', 'Нет')], max_length=200, verbose_name='Парковка')),
                ('description', models.TextField(verbose_name='Полное описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Стоимость')),
                ('status', models.CharField(choices=[('В работе', 'В работе'), ('Приостановлено', 'Приостановлено'), ('Закончено', 'Закончено')], max_length=50, verbose_name='Статус')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RealEstateApp.category', verbose_name='Категория')),
                ('photo', models.ManyToManyField(blank=True, to='RealEstateApp.photo')),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Риелтор')),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='real_estate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='RealEstateApp.realestate'),
        ),
    ]