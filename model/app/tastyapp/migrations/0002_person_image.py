# Generated by Django 2.1.3 on 2018-11-14 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tastyapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='image',
            field=models.FileField(blank=True, upload_to='post_image'),
        ),
    ]
