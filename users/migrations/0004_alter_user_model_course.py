# Generated by Django 5.0.4 on 2024-06-19 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_college_id_user_model_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='course',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
