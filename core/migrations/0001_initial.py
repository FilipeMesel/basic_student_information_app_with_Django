# Generated by Django 4.2.2 on 2023-10-06 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('classe', models.CharField(max_length=100)),
                ('marks', models.FloatField(default=0.0)),
            ],
        ),
    ]
