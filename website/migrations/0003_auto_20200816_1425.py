# Generated by Django 3.1 on 2020-08-16 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20200816_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body0',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body17',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body4',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body5',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body6',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body8',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body9',
        ),
        migrations.RemoveField(
            model_name='post',
            name='cities_to_go0',
        ),
        migrations.RemoveField(
            model_name='post',
            name='cities_to_go1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='cities_to_go2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='cities_to_go3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='cities_to_go4',
        ),
        migrations.RemoveField(
            model_name='post',
            name='cities_to_go5',
        ),
        migrations.RemoveField(
            model_name='post',
            name='cities_to_go6',
        ),
        migrations.RemoveField(
            model_name='post',
            name='cities_to_go7',
        ),
        migrations.RemoveField(
            model_name='post',
            name='cities_to_go8',
        ),
        migrations.RemoveField(
            model_name='post',
            name='cities_to_go9',
        ),
        migrations.AddField(
            model_name='post',
            name='news_image5',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]