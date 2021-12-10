from rest_framework.permissions import BasePermission


class IsNGO(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'ngo'


class IsVolunteer(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'volunteer'
