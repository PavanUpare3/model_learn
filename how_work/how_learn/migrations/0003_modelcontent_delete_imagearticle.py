# Generated by Django 5.0.6 on 2024-06-24 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('how_learn', '0002_remove_imagearticle_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=23)),
                ('content', models.CharField(max_length=345)),
            ],
        ),
        migrations.DeleteModel(
            name='ImageArticle',
        ),
    ]
