from distutils.command.upload import upload
from django.db import models
from .choices import state, modality, job_type
from django.conf import settings
from arearol.models import Area, Rol
from applicants.models import ApplicantProfile

class EmployerProfile(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employer')
    company_name = models.CharField(
        max_length=100, verbose_name='Nombre de la empresa:')
    description = models.CharField(
        max_length=500, verbose_name='Descripción:')
    logo = models.ImageField(upload_to="logo:")

    def company(self):
        return "{}".format(self.company_name)
    
    def __str__(self):
        return self.company() 
    
    def __unicode__(self,):
        return str(self.logo)
    
    # def __str__(self): 
    #     return self.user.email 
    class Meta:
        verbose_name= 'Empleador'
        verbose_name_plural= 'Empleadores'
        db_table= 'employer'
        ordering=['company_name', 'description', 'logo']   
        
      
# class EmployerVacancyRegistration(models.Model):
#     employer_profile= models.ForeignKey(EmployerProfile, on_delete=models.CASCADE, related_name='register_vacancy')
#     area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name='Área:')
#     rol = models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name='Rol:') 
#     job_type = models.CharField(
#       max_length=100, choices=job_type, default='', verbose_name='Tipo de trabajo:')
#     modality = models.CharField(
#       max_length=50, choices=modality, default='', verbose_name='Modalidad:')
#     job_description = models.CharField(max_length=500, verbose_name='Descripción del puesto:')
#     requierements = models.CharField(max_length=500, verbose_name='Requisitos:')
#     video_explanation = models.URLField(max_length=200, verbose_name='Video explicativo:',)
#     salary = models.CharField( 
#       max_length=50, verbose_name='Sueldo:')
#     question_1 = models.CharField(
#         max_length=500, verbose_name='Pregunta 1:')
#     question_2 = models.CharField(
#         max_length=500, verbose_name='Pregunta 2:')
#     question_3 = models.CharField(
#         max_length=500, verbose_name='Pregunta 3:')
#     state = models.CharField(
#       max_length=30, choices=state, default='', verbose_name='Estado:')
#     municipality = models.CharField(
#       max_length=50, verbose_name='Municipio:')
#     applicants = models.ManyToManyField(ApplicantProfile, through = 'postulations.ApplicantVacancyPostulation')
 
#     def __str__(self): 
#         return self.employer_profile
#     class Meta:
#         db_table= 'employer_vacancy_registration'

