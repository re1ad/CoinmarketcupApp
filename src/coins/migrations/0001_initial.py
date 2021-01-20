# Generated by Django 3.1.5 on 2021-01-20 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('symbol', models.CharField(max_length=50)),
                ('price', models.FloatField(blank=True, default=0)),
                ('rank', models.IntegerField(blank=True, db_index=True, default=0)),
                ('image', models.URLField(blank=True, null=True)),
            ],
            options={
                'ordering': ['rank'],
            },
        ),
    ]