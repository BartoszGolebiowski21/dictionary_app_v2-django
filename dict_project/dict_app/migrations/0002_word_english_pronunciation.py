# Generated by Django 4.2.4 on 2023-08-31 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dict_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='english_pronunciation',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
