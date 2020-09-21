# Generated by Django 3.1 on 2020-09-17 15:16

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vocgui', '0014_auto_20200917_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '300x300', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='cropping'),
        ),
    ]
