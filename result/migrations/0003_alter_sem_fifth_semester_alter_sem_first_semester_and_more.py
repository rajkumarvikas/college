# Generated by Django 5.0.4 on 2024-06-10 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0002_alter_sem_sixth_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sem_fifth',
            name='semester',
            field=models.CharField(default='5', editable=False, max_length=1),
        ),
        migrations.AlterField(
            model_name='sem_first',
            name='semester',
            field=models.CharField(default='1', editable=False, max_length=1),
        ),
        migrations.AlterField(
            model_name='sem_fourth',
            name='semester',
            field=models.CharField(default='4', editable=False, max_length=1),
        ),
        migrations.AlterField(
            model_name='sem_second',
            name='semester',
            field=models.CharField(default='2', editable=False, max_length=1),
        ),
        migrations.AlterField(
            model_name='sem_third',
            name='semester',
            field=models.CharField(default='3', editable=False, max_length=1),
        ),
    ]
