# Generated by Django 4.0.3 on 2023-04-22 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0005_remove_employervacancyregistration_applicants_and_more'),
        ('postulations', '0002_alter_applicantvacancypostulation_unique_together'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ApplicantVacancyPostulation',
        ),
    ]
