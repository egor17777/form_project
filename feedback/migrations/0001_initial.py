# Generated by Django 4.1 on 2022-08-12 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('surname', models.CharField(max_length=60)),
                ('feedback', models.TextField()),
                ('genger', models.CharField(max_length=1)),
                ('rating', models.PositiveIntegerField()),
            ],
        ),
    ]
