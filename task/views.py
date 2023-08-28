from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework import permissions, views, response

from account.models import Account
from task.models import Task, Result, GroupCourse
from account.permissions import IsTeacher, IsStudent
from task.serializers import TaskSerializer, ResultSerializer, GroupSerializer


class GroupViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsTeacher | IsStudent,)
    queryset = GroupCourse.objects.all()
    serializer_class = GroupSerializer

    def get_queryset(self):
        try:
            account = Account.objects.get(username=self.request.user.username)
        except:
            account = None

        return self.queryset.filter(member=account)

    def create(self, request, *args, **kwargs):
        return Response({'detail': 'Method Not Allowed'}, status=405)

    def update(self, request, *args, **kwargs):
        return Response({'detail': 'Method Not Allowed'}, status=405)

    def partial_update(self, request, *args, **kwargs):
        return Response({'detail': 'Method Not Allowed'}, status=405)

    def destroy(self, request, *args, **kwargs):
        return Response({'detail': 'Method Not Allowed'}, status=405)

    @action(detail=True, methods=['post', 'put', 'patch', 'delete'])
    def custom_action(self, request, pk=None):
        return Response({'detail': 'Method Not Allowed'}, status=405)


class TaskViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsTeacher)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request, *args, **kwargs):
        return Response({'detail': 'Method Not Allowed'}, status=405)

    def partial_update(self, request, *args, **kwargs):
        return Response({'detail': 'Method Not Allowed'}, status=405)

    @action(detail=True, methods=['post', 'put', 'patch', 'delete'])
    def custom_action(self, request, pk=None):
        return Response({'detail': 'Method Not Allowed'}, status=405)


class ResultViewSet(ModelViewSet):
    permissions_classes = (permissions.IsAuthenticated, IsStudent)
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def get_queryset(self):
        return self.queryset.filter(student=self.request.user)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)
