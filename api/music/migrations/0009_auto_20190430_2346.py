# Generated by Django 2.2 on 2019-04-30 23:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_auto_20190430_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moroso',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]