# Generated by Django 5.0.2 on 2024-03-03 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Failure',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=255)),
            ],
        ),
    ]