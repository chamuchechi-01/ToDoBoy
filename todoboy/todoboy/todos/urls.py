from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('update/<int:task_id>/status/', views.update_task_status, name='update_task_status'),
    path('tasks/delete/<int:id>/', views.task_delete, name='task_delete'),
]
