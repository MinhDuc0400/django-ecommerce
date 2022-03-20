# Generated by Django 4.0.2 on 2022-03-19 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Electronic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('warranty', models.IntegerField(default=2)),
                ('screenSize', models.FloatField(default=0)),
                ('manufacturer', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('electronic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='electronics.electronic')),
                ('ram', models.CharField(max_length=255)),
                ('cpu', models.CharField(max_length=255)),
                ('card', models.CharField(max_length=255)),
            ],
            bases=('electronics.electronic',),
        ),
        migrations.CreateModel(
            name='MobilePhone',
            fields=[
                ('electronic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='electronics.electronic')),
                ('ram', models.CharField(max_length=255)),
                ('cpu', models.CharField(max_length=255)),
                ('camera', models.CharField(max_length=255)),
            ],
            bases=('electronics.electronic',),
        ),
        migrations.CreateModel(
            name='Tivi',
            fields=[
                ('electronic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='electronics.electronic')),
                ('connector', models.CharField(max_length=255)),
            ],
            bases=('electronics.electronic',),
        ),
        migrations.CreateModel(
            name='ElectronicItem',
            fields=[
                ('barCode', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('price', models.FloatField(default=0)),
                ('discount', models.FloatField(default=0)),
                ('img', models.ImageField(upload_to='electronics/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('electronic', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='electronics.electronic')),
            ],
        ),
    ]