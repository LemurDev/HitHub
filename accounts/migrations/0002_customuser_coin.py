# Generated by Django 5.0 on 2024-01-08 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='coin',
            field=models.DecimalField(decimal_places=2, default=1000.0, max_digits=100),
        ),
    ]