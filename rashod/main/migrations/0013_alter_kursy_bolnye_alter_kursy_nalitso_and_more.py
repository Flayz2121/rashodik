# Generated by Django 5.1.3 on 2025-02-03 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_otpusks_info_of_otpusks_10_mesto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kursy',
            name='bolnye',
            field=models.IntegerField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='kursy',
            name='naLitso',
            field=models.IntegerField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='kursy',
            name='naryad',
            field=models.IntegerField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='kursy',
            name='otpusk',
            field=models.IntegerField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='kursy',
            name='poSpisku',
            field=models.IntegerField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='kursy',
            name='uvolnenie',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
