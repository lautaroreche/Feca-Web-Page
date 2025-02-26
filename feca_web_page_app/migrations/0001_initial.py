# Generated by Django 5.1.6 on 2025-02-25 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('Cafe', 'Cafe'), ('Panaderia', 'Panaderia'), ('Comida', 'Comida'), ('Bebida', 'Bebida'), ('Otro', 'Otro')], max_length=20)),
            ],
        ),
    ]
