from django.urls import path
from . import views
from compare_code.routers import CustomRouter

router = CustomRouter(root_view_name='task-root')
router.register(r'task', views.TaskViewSet, basename='task')
router.register(r'group', views.GroupViewSet, basename='group')
router.register(r'result', views.ResultViewSet, basename='result')

urlpatterns = router.urls
