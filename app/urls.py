from django.urls import path, include
from .views import TaskViewSet, TeacherViewSet, LessonViewSet, LessonPartViewSet, ModuleViewSet, SpecialityViewSet, CourseViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('speciality', SpecialityViewSet)
router.register('courses', CourseViewSet)
router.register('module', ModuleViewSet)
router.register('lesson', LessonViewSet)
router.register('lesson-part', LessonPartViewSet)
router.register('teachers', TeacherViewSet)
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', obtain_auth_token),
]