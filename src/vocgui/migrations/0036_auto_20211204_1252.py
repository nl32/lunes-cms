# Generated by Django 3.2.7 on 2021-12-04 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocgui', '0035_auto_20211204_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingset',
            name='discipline',
            field=models.ManyToManyField(related_name='training_sets', to='vocgui.Discipline', verbose_name='discipline'),
        ),
        migrations.AlterField(
            model_name='trainingset',
            name='documents',
            field=models.ManyToManyField(related_name='training_sets', to='vocgui.Document', verbose_name='document'),
        ),
    ]