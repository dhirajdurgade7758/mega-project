# Generated by Django 5.0.3 on 2024-03-12 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_alter_semisters_sem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semisters',
            name='sem',
            field=models.IntegerField(),
        ),
    ]
