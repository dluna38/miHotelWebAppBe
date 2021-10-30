# Generated by Django 3.2.7 on 2021-10-21 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='check_id',
            new_name='check_in',
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_status',
            field=models.CharField(default='POR PAGAR', max_length=30),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_type',
            field=models.CharField(default='EFECTIVO', max_length=100),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='num_guess',
            field=models.SmallIntegerField(default=1),
        ),
    ]