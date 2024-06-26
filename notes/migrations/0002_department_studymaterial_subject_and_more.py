# Generated by Django 5.0.3 on 2024-03-10 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=50)),
                ('icon', models.ImageField(upload_to='icons')),
            ],
        ),
        migrations.CreateModel(
            name='StudyMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('NOTES', 'Notes'), ('BOOKS', 'Books'), ('MODEL_QP', 'Model question papers'), ('MODEL_ANS', 'Model ans papers'), ('MICRO_PROJECTS', 'Micro-projects')], max_length=20)),
                ('description', models.CharField(max_length=300)),
                ('semister', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='files')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=50)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.department')),
            ],
        ),
        migrations.DeleteModel(
            name='studyMaterials',
        ),
        migrations.AddField(
            model_name='studymaterial',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.subject'),
        ),
    ]
