from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    
    path('create/',views.add_and_show,name='create'),
    path('del/<int:id>/',views.delete_teacher,name='delete'),
    path('update/<int:id>/',views.update_teacher,name='update')
    
]
