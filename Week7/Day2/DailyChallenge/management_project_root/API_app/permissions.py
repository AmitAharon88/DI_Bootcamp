from rest_framework import permissions

class IsDepartmentAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and obj.department.admin == request.user:
            return True
        else :
            return False