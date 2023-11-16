# Generated by Django 4.2.5 on 2023-11-02 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=254)),
                ('parameters', models.CharField(blank=True, default='', max_length=254)),
                ('description', models.CharField(blank=True, default='', max_length=254)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]