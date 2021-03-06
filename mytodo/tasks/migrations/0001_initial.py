# Generated by Django 3.0.6 on 2020-05-18 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=160)),
                ('deadline', models.DateTimeField(verbose_name='deadline')),
                ('done', models.FloatField(default=0.0)),
            ],
        ),
    ]
