# Generated by Django 3.1b1 on 2021-06-02 14:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tobi', '0002_auto_20210528_2353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='code',
            old_name='author',
            new_name='person',
        ),
        migrations.AddField(
            model_name='person',
            name='picture',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_details', models.CharField(max_length=300)),
                ('project', models.FileField(upload_to='')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tobi.code')),
            ],
        ),
    ]
