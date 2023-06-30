from rest_framework import permissions


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.all()[0].name == 'teacher'


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.all()[0].name == 'student'
