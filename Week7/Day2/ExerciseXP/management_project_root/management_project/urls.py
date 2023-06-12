from django.contrib import admin
from django.urls import path, include
from API_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('departments/', DepartmentListAPIView.as_view(), name='department-list'),
    path('departments/create', DepartmentCreateAPIView.as_view(), name='department-create'),
    path('employee/', EmployeeListAPIView.as_view(), name='employee-list'),
    path('employee/create', EmployeeCreateAPIView.as_view(), name='employee-create'),
    path('project/<int:pk>/', ProjectRetrieveAPIView.as_view(), name='project-instance'),
    path('project/<int:pk>/update', ProjectUpdateAPIView.as_view(), name='project-update'),
    path('project/<int:pk>/delete', ProjectDestroyAPIView.as_view(), name='project-delete'),
    path('task/<int:pk>/', TaskRetrieveAPIView.as_view(), name='Task-instance'),
    path('task/<int:pk>/update', TaskUpdateAPIView.as_view(), name='task-update'),
    path('task/<int:pk>/delete', TaskDestroyAPIView.as_view(), name='task-delete'),
]
