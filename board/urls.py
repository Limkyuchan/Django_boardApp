from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.board, name='board'),
    path('add/', views.add, name="add"),
    path('list/', views.list, name='list'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
]
