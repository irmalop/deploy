# Generated by Django 4.0.3 on 2022-07-20 11:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('Curso', 'Curso'), ('Certificacion', 'Certificacion'), ('Carrera técnica', 'Carrera técnica'), ('Universidad', 'Universidad'), ('Maestria', 'Maestria'), ('Doctorado', 'Doctorado')], default='', max_length=30, verbose_name='Nivel')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('institution', models.CharField(max_length=100, verbose_name='Institución')),
                ('duration', models.CharField(max_length=50, verbose_name='Duración')),
                ('status', models.CharField(choices=[('Finalizado', 'Finalizado'), ('Trunco', 'Trunco'), ('En curso', 'En curso')], default='', max_length=20, verbose_name='Estatus')),
            ],
            options={
                'db_table': 'applicant_academic_data',
            },
        ),
        migrations.CreateModel(
            name='ApplicantJobInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modality', models.CharField(choices=[('Presencial', 'Presencial'), ('Home office', 'Home office'), ('Híbrido', 'Híbrido')], default='', max_length=20, verbose_name='Modalidad:')),
                ('job_type', models.CharField(choices=[('Tiempo completo', 'Tiempo completo'), ('Medio tiempo', 'Medio tiempo')], default='', max_length=20, verbose_name='Tipo de trabajo:')),
            ],
            options={
                'db_table': 'applicant_job_interest',
            },
        ),
        migrations.CreateModel(
            name='ApplicantProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paternal_surname', models.CharField(max_length=20, verbose_name='Apellido paterno:')),
                ('maternal_surname', models.CharField(max_length=20, verbose_name='Apellido materno:')),
                ('name', models.CharField(max_length=20, verbose_name='Nombre(s):')),
                ('sex', models.CharField(choices=[('Mujer', 'Mujer'), ('Hombre', 'Hombre'), ('Prefiero no responder', 'Prefiero no responder')], default='', max_length=30, verbose_name='Sexo:')),
                ('date_of_birth', models.DateField(verbose_name='Fecha de nacimiento:')),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(99)], verbose_name='Edad:')),
                ('marital_status', models.CharField(choices=[('Soltero', 'Soltero'), ('Casado', 'Casado'), ('Viudo', 'Viudo'), ('Divorciado', 'Divorciado'), ('Unión libre', 'Unión libre'), ('Prefiero no responder', 'Prefiero no responder')], default='', max_length=30, verbose_name='Estado civil:')),
                ('email', models.EmailField(max_length=200, verbose_name='Correo electrónico:')),
                ('state', models.CharField(choices=[('AGS', 'Aguascalientes'), ('BCN', 'Baja California'), ('BCS', 'Baja California Sur'), ('CAM', 'Campeche'), ('CHP', 'Chiapas'), ('CHI', 'Chihuahua'), ('CMX', 'Ciudad de México'), ('COA', 'Coahuila'), ('COL', 'Colima'), ('DUR', 'Durango'), ('GTO', 'Guanajuato'), ('GRO', 'Guerrero'), ('HGO', 'Hidalgo'), ('JAL', 'Jalisco'), ('MEX', 'Estado de México'), ('MIC', 'Michoacán'), ('MOR', 'Morelos'), ('NAY', 'Nayarit'), ('NLE', 'Nuevo León'), ('OAX', 'Oaxaca'), ('PUE', 'Puebla'), ('QRO', 'Querétaro'), ('ROO', 'Quintana Roo'), ('SLP', 'San Luis Potosí'), ('SIN', 'Sinaloa'), ('SON', 'Sonora'), ('TAB', 'Tabasco'), ('TAM', 'Tamaulipas'), ('TLX', 'Tlaxcala'), ('VER', 'Veracruz'), ('YUC', 'Yucatán'), ('ZAC', 'Zacatecas')], default='', max_length=30, verbose_name='Estado de residencia:')),
                ('municipality', models.CharField(max_length=20, verbose_name='Municipio de residencia:')),
            ],
            options={
                'verbose_name': 'Aplicante',
                'verbose_name_plural': 'Aplicantes',
                'db_table': 'applicant',
                'ordering': ['paternal_surname', '-maternal_surname'],
            },
        ),
        migrations.CreateModel(
            name='ApplicantVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.URLField(verbose_name='video')),
            ],
            options={
                'db_table': 'applicant_video',
            },
        ),
    ]
