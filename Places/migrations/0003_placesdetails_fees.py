# Generated by Django 3.2.9 on 2022-06-25 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Places', '0002_auto_20220624_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='placesdetails',
            name='fees',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
