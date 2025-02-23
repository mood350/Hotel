# Generated by Django 5.1.6 on 2025-02-23 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_chambrehotel_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chambrehotel',
            name='type',
            field=models.CharField(choices=[(0, 'Simple'), (1, 'Double'), (2, 'Suite')], default=0),
        ),
    ]
