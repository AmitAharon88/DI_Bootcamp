from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics

# Create your views here.
class DepartmentListAPIView(generics.ListAPIView):
   queryset = Department.objects.all()
   serializer_class = DepartmentSerializer

class DepartmentCreateAPIView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeListAPIView(generics.ListAPIView):
   queryset = Employee.objects.all()
   serializer_class = EmployeeSerializer

class EmployeeCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ProjectRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer