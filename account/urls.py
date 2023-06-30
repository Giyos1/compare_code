from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='user-logout'),
    path('session/', views.SessionUserView.as_view(), name='session'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('teacher/page/', views.TeacherPageView.as_view(), name='teacher-page'),
    path('student/page/', views.StudentPageView.as_view(), name='student-page'),
]
