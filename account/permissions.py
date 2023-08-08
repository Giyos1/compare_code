from rest_framework import permissions


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            return request.user.groups.all()[0].name == 'teacher'
        except:
            return False


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            return request.user.groups.all()[0].name == 'student'
        except:
            return False
