# Generated by Django 3.2.6 on 2021-09-06 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puppies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='puppy',
            options={'verbose_name_plural': 'puppies'},
        ),
    ]
