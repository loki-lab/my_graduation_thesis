# Generated by Django 4.2.3 on 2023-07-25 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0004_alter_comment_date_alter_comment_mriimages_profile"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="historypatient",
            name="PatientID",
        ),
        migrations.RemoveField(
            model_name="medicalappointmentschedule",
            name="DoctorID",
        ),
        migrations.RemoveField(
            model_name="medicalappointmentschedule",
            name="ReceptionistID",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="MRIImages",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="ResultByAI",
        ),
        migrations.RemoveField(
            model_name="patient",
            name="Image",
        ),
        migrations.AddField(
            model_name="comment",
            name="InputImage",
            field=models.ImageField(blank=True, null=True, upload_to="media/"),
        ),
        migrations.AddField(
            model_name="comment",
            name="OutputImage",
            field=models.ImageField(blank=True, null=True, upload_to="media/"),
        ),
        migrations.AddField(
            model_name="patient",
            name="images",
            field=models.ImageField(blank=True, null=True, upload_to="media/"),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="Image",
            field=models.ImageField(blank=True, null=True, upload_to="media/"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="profile_image",
            field=models.ImageField(blank=True, null=True, upload_to="media/"),
        ),
        migrations.DeleteModel(
            name="diseaseprogression",
        ),
        migrations.DeleteModel(
            name="historypatient",
        ),
        migrations.DeleteModel(
            name="medicalappointmentschedule",
        ),
    ]
