# Generated by Django 3.1b1 on 2021-09-24 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tobi', '0004_code_lang_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='project',
            field=models.TextField(),
        ),
    ]
