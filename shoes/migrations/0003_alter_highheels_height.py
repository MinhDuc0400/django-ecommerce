# Generated by Django 4.0.3 on 2022-03-20 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0002_alter_highheels_height'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highheels',
            name='height',
            field=models.FloatField(default=0),
        ),
    ]