# Generated by Django 3.0.6 on 2020-05-06 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foyer_france', '0004_command_dateofcommand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='dateOfCommand',
            field=models.DecimalField(decimal_places=10, default=1588808305.7079139, max_digits=20),
        ),
    ]
