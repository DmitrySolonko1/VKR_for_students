# Generated by Django 4.1.7 on 2023-05-21 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RealEstateApp', '0003_timeslot_alter_realestate_price_booking'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'Бронь', 'verbose_name_plural': 'Бронь'},
        ),
        migrations.AlterModelOptions(
            name='timeslot',
            options={'verbose_name': 'Время бронирования', 'verbose_name_plural': 'Время бронирования'},
        ),
        migrations.AddField(
            model_name='realestate',
            name='latitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Ширина'),
        ),
        migrations.AddField(
            model_name='realestate',
            name='longitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='finishing',
            field=models.CharField(choices=[('Без отделки', 'Без отделки'), ('под чистовую отделку', 'под чистовую отделку'), ('Косметический', 'Косметический'), ('Капитальный', 'Капитальный'), ('евроремонт', 'евроремонт'), ('дизайнерский', 'дизайнерский'), ('ремонт премиум-класса', 'ремонт премиум-класса')], max_length=70, verbose_name='Ремонт'),
        ),
    ]