# Generated by Django 4.0.4 on 2022-05-04 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('function', '0023_remove_userjourneydata_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userjourneydata',
            name='key',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userjourneydata',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]