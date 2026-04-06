from rest_framework.permissions import BasePermission


# custom role based permissions
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class IsAnalyst(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['admin', 'analyst']

class IsViewer(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['admin', 'analyst', 'viewer']