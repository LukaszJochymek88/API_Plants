# Generated by Django 3.0.2 on 2020-02-08 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='Nazwa kategori', max_length=100, unique=True, verbose_name='Nazwa')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='Rodzaj Pokoju', max_length=100, unique=True, verbose_name='Nazwa')),
                ('temperature', models.CharField(choices=[('COLD', 'cold'), ('MEDIUM', 'medium'), ('WARM', 'warm')], max_length=10, verbose_name='Temperature')),
                ('exposure', models.CharField(choices=[('DARK', 'dark'), ('SHADE', 'shade'), ('PARTSUN', 'part sun'), ('FULLSUN', 'full sun')], max_length=10, verbose_name='Ekspozycja')),
                ('humidity', models.CharField(choices=[('LOW', 'low'), ('MEDIUM', 'medium'), ('HIGH', 'high')], max_length=10, verbose_name='Humidity')),
                ('draft', models.BooleanField(blank=True, default=False, verbose_name='Drafty?')),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nazwa Rośliny', max_length=100, unique=True, verbose_name='Nazwa Rośliny')),
                ('watering_interval', models.PositiveIntegerField(default='', help_text='dni', verbose_name='Okres podlewania')),
                ('fertilizing_interval', models.PositiveIntegerField(help_text='dni', verbose_name='Okres nawożenia')),
                ('required_exposure', models.CharField(choices=[('DARK', 'dark'), ('SHADE', 'shade'), ('PARTSUN', 'part sun'), ('FULLSUN', 'full sun')], max_length=10, verbose_name='Ekspozycja')),
                ('required_humidity', models.CharField(choices=[('LOW', 'low'), ('MEDIUM', 'medium'), ('HIGH', 'high')], max_length=10, verbose_name='Ekspozycja')),
                ('required_temperature', models.CharField(choices=[('COLD', 'cold'), ('MEDIUM', 'medium'), ('WARM', 'warm')], max_length=10, verbose_name='Temperatura')),
                ('blooming', models.BooleanField(blank=True, default=False, verbose_name='Blooming?')),
                ('defficulty', models.PositiveIntegerField(choices=[(1, 'Low'), (2, 'Medium-Low'), (3, 'Medium'), (4, 'Medium-high'), (5, 'High')], default=1, verbose_name='Cultivation difficulty level')),
                ('last_watered', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Ostatnie Podlanie')),
                ('last_fertilized', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Ostatnie nawożenie')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='plants.Category', verbose_name="Plant's category")),
                ('room', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='plants.Room', verbose_name="Plant's room")),
            ],
        ),
    ]
