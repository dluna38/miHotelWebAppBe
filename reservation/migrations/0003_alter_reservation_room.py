# Generated by Django 3.2.7 on 2021-10-30 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20211029_1958'),
        ('reservation', '0002_auto_20211021_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.rooms'),
        ),
    ]