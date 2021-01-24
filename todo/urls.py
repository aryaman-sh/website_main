from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
    path('', views.index, name="index"),
    path('add_todo/', views.add_todo, name="add_todo"),
    path('delete_todo/<int:del_id>/', views.delete, name="delete"),
    path('update/<int:update_id>/', views.update, name="update"),
]