# Generated by Django 3.2rc1 on 2021-03-23 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocgui', '0011_trainingset_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alternativeword',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='document',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trainingset',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]