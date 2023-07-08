from django.contrib.auth.models import User
from rest_framework import views, response, permissions
from django.contrib.auth import login, logout
from .authentication import CsrfExemptSessionAuthentication
from .serializers import LoginSerializer, UserSerializer, RegisterationSerializer
from .permissions import IsTeacher, IsStudent


class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return response.Response(UserSerializer(user).data)


class LogoutView(views.APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, ]
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        logout(request)
        return response.Response(data={'message': 'logout success'}, status=200)


class SessionUserView(views.APIView):

    def get(self, request):
        user = User.objects.get(pk=self.request.user.id)
        serializer = UserSerializer(user)
        return response.Response(data=serializer.data)


class RegistrationView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = RegisterationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(data=serializer.data, status=201)


class TeacherPageView(views.APIView):
    permission_classes = (IsTeacher,)

    def get(self, request):
        return response.Response(data={'message': 'teacher page'}, status=200)


class StudentPageView(views.APIView):
    permission_classes = (IsStudent,)

    def get(self, request):

        return response.Response(data={'message': 'student page'}, status=200)
