# Generated by Django 5.0.4 on 2024-05-02 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=100)),
                ('medicine_description', models.CharField(max_length=255)),
                ('medicine_price', models.CharField(max_length=255)),
            ],
        ),
    ]
