# Generated by Django 4.1.4 on 2023-01-09 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automotor',
            name='stock',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='electrodomesticos',
            name='stock',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='herramientas',
            name='stock',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='hogar',
            name='stock',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='indumentaria',
            name='stock',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='perfumeria',
            name='stock',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='tecnologia',
            name='stock',
            field=models.BooleanField(default=True),
        ),
    ]
