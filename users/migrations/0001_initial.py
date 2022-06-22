# Generated by Django 4.0.5 on 2022-06-22 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=45)),
                ('account', models.CharField(max_length=128, unique=True)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('phone_number', models.CharField(max_length=45, unique=True)),
                ('password', models.CharField(max_length=500)),
                ('point', models.DecimalField(decimal_places=2, default=100000.0, max_digits=8)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]