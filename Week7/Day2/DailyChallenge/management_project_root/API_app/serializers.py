from rest_framework import serializers
from .models import *

class DepartmentSerializer(serializers.HyperlinkedModelSerializer) :
    # url = serializers.HyperlinkedIdentityField(view_name='department-detail')
    class Meta :
        model = Department
        fields = ('name', 'description', 'url')
        
class EmployeeSerializer(serializers.HyperlinkedModelSerializer) :
    url = serializers.HyperlinkedIdentityField(view_name='employee-detail')
    class Meta :
        model = Employee
        fields = ('id', 'name', 'email', 'phone_number', 'projects', 'url')
        
class TaskSerializer(serializers.HyperlinkedModelSerializer) :
    url = serializers.HyperlinkedIdentityField(view_name='task-detail')
    class Meta :
        model = Task
        fields = ('name', 'description', 'due_date', 'completed', 'project', 'url')

class ProjectSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Project
        fields = ('name', 'description', 'start_date', 'end_date')