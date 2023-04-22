from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
   def has_permission(self, request, view):
      return request.user.is_admin

class IsApplicant(BasePermission):
   def has_permission(self, request, view):
      return request.user.is_applicant

class IsEmployer(BasePermission):
   def has_permission(self, request, view):
      return request.user.is_employer
      