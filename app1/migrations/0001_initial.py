# Generated by Django 3.0.2 on 2020-01-18 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=100)),
                ('prod_detail', models.CharField(max_length=100)),
                ('prod_qty', models.PositiveIntegerField(default=0)),
                ('prod_price', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
