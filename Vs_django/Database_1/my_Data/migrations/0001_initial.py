# Generated by Django 3.2.5 on 2021-07-26 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_Name', models.CharField(max_length=20)),
                ('item_Cost', models.FloatField()),
            ],
        ),
    ]
