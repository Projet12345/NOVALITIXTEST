# Generated by Django 4.2.8 on 2023-12-06 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novalitix', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictiondata',
            name='PREDICTION',
            field=models.FloatField(null=True),
        ),
    ]
