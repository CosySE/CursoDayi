from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path('add', views.add_person, name= 'add_person'),
    path('delete/<int:person_id>/', views.delete_person, name= 'delete_person'),
    path('update/<int:person_id>/', views.update_person, name= 'update_person'),



]