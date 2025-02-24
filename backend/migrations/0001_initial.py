# Generated by Django 5.1.6 on 2025-02-22 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChambreHotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroChambre', models.IntegerField(unique=True)),
                ('type', models.CharField(max_length=50)),
                ('prix', models.PositiveIntegerField()),
                ('petit_dejeuner', models.BooleanField(default=False)),
                ('etage', models.IntegerField()),
                ('description', models.TextField()),
                ('disponibilite', models.BooleanField(default=True)),
            ],
        ),
    ]
