# Generated by Django 3.1.5 on 2021-03-07 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=True, upload_to='post_pic'),
        ),
    ]
