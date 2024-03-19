# Generated by Django 5.0.3 on 2024-03-10 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_alter_studymaterial_semister'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studymaterial',
            name='description',
        ),
        migrations.AddField(
            model_name='subject',
            name='semister',
            field=models.CharField(choices=[('first', 'First sem'), ('second', 'Second sem'), ('third', 'Third sem'), ('fourth', 'Fourth sem'), ('fifth', 'Fifth sem'), ('sixth', 'sixth sem')], default=None, max_length=50),
        ),
    ]
