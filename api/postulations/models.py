from django.db import models
from applicants.models import ApplicantProfile
# from employers.models import EmployerVacancyRegistration

# # Create your models here.
# class  ApplicantVacancyPostulation(models.Model):
#     vacancy = models.ForeignKey(EmployerVacancyRegistration, on_delete=models.CASCADE, related_name='postulated_vacancy')
#     applicant = models.ForeignKey(ApplicantProfile, on_delete=models.CASCADE, related_name='postulated_applicant')
#     postulated_time = models.DateTimeField(auto_now_add=True)
#     link_video = models.URLField(max_length=200, verbose_name='link_video')

#     class Meta:
#         db_table= 'postulations'
#         verbose_name_plural = 'Postulations'
#         unique_together = ('applicant', 'vacancy')
