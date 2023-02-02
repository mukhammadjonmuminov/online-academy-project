from rest_framework.viewsets import ModelViewSet
from .models import Task, Teacher, LessonPart, Lesson, Module, Course, Speciality
from .serializers import TaskSerializer, TeacherSerializer, LessonSerializer, LessonPartSerializer, ModuleSerializer, CourseSerializer, SpecialitySerializer
from rest_framework.pagination import LimitOffsetPagination
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

class SpecialityViewSet(ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
    # permission_classes = [IsAuthenticated, ]
    # authentication_classes = [TokenAuthentication, ]
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', ]
    ordering_fields = ['title', ]

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = [IsAuthenticated, ]
    # authentication_classes = [TokenAuthentication, ]
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', ]

class ModuleViewSet(ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    # permission_classes = [IsAuthenticated, ]
    # authentication_classes = [TokenAuthentication, ]
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', ]

class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    # permission_classes = [IsAuthenticated, ]
    # authentication_classes = [TokenAuthentication, ]
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', ]

class LessonPartViewSet(ModelViewSet):
    queryset = LessonPart.objects.all()
    serializer_class = LessonPartSerializer
    # permission_classes = [IsAuthenticated, ]
    # authentication_classes = [TokenAuthentication, ]
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', ]

class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [IsAuthenticated, ]
    # authentication_classes = [TokenAuthentication, ]
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', ]

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated, ]
    # authentication_classes = [TokenAuthentication, ]
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', ]