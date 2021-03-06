# Generated by Django 3.1 on 2020-08-19 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20200816_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('hotel_image2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('hotel_image3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('hotel_image4', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('hotel_name', models.CharField(max_length=255)),
                ('hotel_price', models.CharField(max_length=255)),
                ('hotel_address', models.CharField(max_length=255)),
                ('hotel_description', models.TextField()),
                ('hotel_to_center', models.CharField(max_length=255)),
                ('hotel_to_airport', models.CharField(max_length=255)),
                ('hotel_near_sightseeings', models.CharField(max_length=255)),
            ],
        ),
    ]
