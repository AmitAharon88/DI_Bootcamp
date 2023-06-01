from django.contrib import admin
from django.urls import path
from todo.views import (add_category_view,
                        add_todo_view,
                        display_todos)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-category/', add_category_view),
    path('add-todo/', add_todo_view),
    path('todos/', display_todos)
]
