# Generated by Django 3.1.3 on 2021-04-04 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0011_auto_20210403_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.ImageField(default='user-icon.png', upload_to=''),
        ),
    ]