# Generated by Django 3.0.3 on 2020-05-08 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomProduit', models.CharField(max_length=40)),
                ('quantitemax', models.IntegerField()),
                ('prix', models.IntegerField()),
            ],
        ),
    ]
