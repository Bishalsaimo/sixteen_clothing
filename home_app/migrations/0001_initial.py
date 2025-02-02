# Generated by Django 5.0.3 on 2024-03-26 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('desc', models.TextField()),
                ('reviews', models.IntegerField()),
            ],
        ),
    ]
