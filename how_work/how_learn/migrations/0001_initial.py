# Generated by Django 5.0.6 on 2024-06-24 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=250)),
                ('image', models.ImageField(upload_to='my_imagess')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
