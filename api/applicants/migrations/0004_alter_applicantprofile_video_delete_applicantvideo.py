# Generated by Django 4.0.3 on 2022-07-25 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0003_applicantprofile_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantprofile',
            name='video',
            field=models.URLField(default='', verbose_name='Video'),
        ),
        migrations.DeleteModel(
            name='ApplicantVideo',
        ),
    ]
