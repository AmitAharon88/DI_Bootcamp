from django.urls import path
from students.views import StudentView, StudentDetailView

urlpatterns = [
    path('', StudentView.as_view(), name='students'),
    path('<int:pk>', StudentDetailView.as_view(), name='student')
]