# Generated by Django 3.1.3 on 2021-04-05 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_article_updated_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Alert',
        ),
        migrations.RemoveField(
            model_name='web',
            name='articles',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Web',
        ),
    ]
