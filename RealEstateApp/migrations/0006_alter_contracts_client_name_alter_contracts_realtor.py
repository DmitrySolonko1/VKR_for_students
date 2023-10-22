# Generated by Django 4.1.7 on 2023-06-05 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RealEstateApp', '0005_contracts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contracts',
            name='client_name',
            field=models.ForeignKey(limit_choices_to={'is_staff': False}, on_delete=django.db.models.deletion.CASCADE, related_name='contract_client', to=settings.AUTH_USER_MODEL, verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='contracts',
            name='realtor',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, related_name='contract_rieltor', to=settings.AUTH_USER_MODEL, verbose_name='Риелтор'),
        ),
    ]
