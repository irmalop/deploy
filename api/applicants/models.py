from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from .choices import sex, marital_status, state, LEVEL, STATUS, modality, job_type
from arearol.models import Area, Rol


class ApplicantVideo(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    video= models.URLField(max_length=200, verbose_name='video',)
    def __str__(self): 
        return self.user.email
    class Meta: 
        db_table='applicant_video'

class ApplicantProfile(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applicant')
    paternal_surname = models.CharField(max_length=20, verbose_name='Apellido paterno:')
    maternal_surname = models.CharField(max_length=20, verbose_name='Apellido materno:')
    name = models.CharField(max_length=20, verbose_name='Nombre(s):')
    sex = models.CharField(max_length=30, choices=sex, default='', verbose_name='Sexo:')
    date_of_birth = models.DateField(verbose_name='Fecha de nacimiento:')
    age = models.IntegerField(
      validators=[MinValueValidator(18), MaxValueValidator(99)], verbose_name='Edad:')
    marital_status = models.CharField(
      max_length=30, choices=marital_status, default='', verbose_name='Estado civil:')
    email = models.EmailField(max_length=200, verbose_name='Correo electrónico:')
    state = models.CharField(max_length=30, choices=state, default='', verbose_name='Estado de residencia:')
    municipality = models.CharField(max_length=20, verbose_name='Municipio de residencia:')
    
    def __str__(self): 
        return self.user.email   
    class Meta:
        verbose_name= 'Aplicante'
        verbose_name_plural= 'Aplicantes'
        db_table= 'applicant'
        ordering=['paternal_surname', '-maternal_surname'] 
        
class AcademicData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='academic')
    level = models.CharField(max_length=30, choices=LEVEL, default='', verbose_name='Nivel')
    name = models.CharField(max_length=50, verbose_name='Nombre')
    institution = models.CharField(max_length=100, verbose_name='Institución')
    duration = models.CharField(max_length=50, verbose_name='Duración')
    status = models.CharField(max_length=20, choices=STATUS, default='', verbose_name='Estatus')
    def __str__(self): 
        return self.user.email
    class Meta:
        db_table='applicant_academic_data'
        
      
class ApplicantJobInterest(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='job_interest')
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name='Area:')
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name='Rol:') 
    modality = models.CharField(
      max_length=20, choices=modality, default='', verbose_name='Modalidad:')
    job_type = models.CharField(
      max_length=20, choices=job_type, default='', verbose_name='Tipo de trabajo:')
     
    def __str__(self): 
        return self.user.email   
    class Meta:
        db_table= 'applicant_job_interest'
  


