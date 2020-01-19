# Generated by Django 2.2.9 on 2020-01-18 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Headline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=500)),
                ('newspaper', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('link', models.CharField(max_length=1000)),
                ('day_order', models.PositiveIntegerField()),
            ],
        ),
    ]
