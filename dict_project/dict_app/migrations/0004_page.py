# Generated by Django 4.2.4 on 2023-09-08 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dict_app', '0003_alter_word_english_translation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=80)),
                ('visits_count', models.IntegerField(default=0)),
            ],
        ),
    ]
