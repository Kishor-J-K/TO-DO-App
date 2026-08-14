from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addTask/', views.add_task, name='add_task'),
    path('mark_as_done/<int:id>/', views.mark_as_done, name='mark_as_done'),
    path('delete_task/<int:id>/', views.delete_task, name='delete_task'),
    path('edit_task/<int:id>/', views.edit_task, name='edit_task'),
    path('mark_as_undone/<int:id>/', views.mark_as_undone, name='mark_as_undone'),
]