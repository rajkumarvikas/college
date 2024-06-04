# Generated by Django 5.0.4 on 2024-05-30 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Model',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('registration_id', models.CharField(max_length=15)),
                ('college_id', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('role', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Qualifications_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30)),
                ('year', models.CharField(max_length=9)),
                ('school', models.CharField(max_length=300)),
                ('roll_code', models.CharField(max_length=10)),
                ('total_marks', models.CharField(max_length=3)),
                ('obtain_marks', models.CharField(max_length=3)),
                ('rid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user_model')),
            ],
        ),
        migrations.CreateModel(
            name='Personal_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(max_length=50)),
                ('mother_name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=15)),
                ('cast', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('nationality', models.CharField(max_length=30)),
                ('pwd', models.BooleanField()),
                ('rid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user_model')),
            ],
        ),
        migrations.CreateModel(
            name='Document_Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.CharField(max_length=500)),
                ('signatue_url', models.CharField(max_length=500)),
                ('adhar_url', models.CharField(max_length=500)),
                ('tenth_url', models.CharField(max_length=500)),
                ('twelth_url', models.CharField(max_length=500)),
                ('rid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user_model')),
            ],
        ),
        migrations.CreateModel(
            name='Document_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='documentation/photo/')),
                ('signatue', models.ImageField(upload_to='documentation/signature/')),
                ('adhar', models.FileField(upload_to='documentation/adhar/')),
                ('tenth', models.FileField(upload_to='documentation/tenth/')),
                ('twelth', models.FileField(upload_to='documentation/twelth/')),
                ('rid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user_model')),
            ],
        ),
        migrations.CreateModel(
            name='Address_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_number', models.IntegerField()),
                ('locality', models.CharField(max_length=50)),
                ('sublocality', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6)),
                ('contract_number', models.CharField(max_length=10)),
                ('alternate_number', models.CharField(max_length=10)),
                ('rid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user_model')),
            ],
        ),
    ]