# Generated by Django 4.2.1 on 2023-06-04 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_trabajador_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajador',
            name='salary',
            field=models.FloatField(default=0),
        ),
    ]
