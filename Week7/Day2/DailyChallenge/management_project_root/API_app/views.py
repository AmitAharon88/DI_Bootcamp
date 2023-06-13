from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsDepartmentAdmin

# Create your views here.
class DepartmentListAPIView(generics.ListAPIView):
   queryset = Department.objects.all()
   serializer_class = DepartmentSerializer
   permission_classes = (IsDepartmentAdmin, )

class DepartmentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (IsDepartmentAdmin, )

class DepartmentCreateAPIView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeListAPIView(generics.ListAPIView):
   queryset = Employee.objects.all()
   serializer_class = EmployeeSerializer
   permission_classes = (IsDepartmentAdmin, )

class EmployeeRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsDepartmentAdmin, )
    
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

class TaskListAPIView(generics.ListAPIView):
   queryset = Task.objects.all()
   serializer_class = TaskSerializer
   permission_classes = (IsDepartmentAdmin, )
   
class TaskRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsDepartmentAdmin, )

class TaskUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer