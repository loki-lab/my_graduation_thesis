# Generated by Django 4.1 on 2023-07-26 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_historypatient_patientid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='InputImage',
            field=models.ImageField(blank=True, null=True, upload_to='InputImages/'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='OutputImage',
            field=models.ImageField(blank=True, null=True, upload_to='OutputImages/'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='docterImages/'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ExamDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='PatientImages/'),
        ),
    ]
