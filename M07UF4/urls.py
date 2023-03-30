from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index_one'),
    path('teachers', views.teachers,name='teachers'),
    path('students', views.students, name='students'),
    # path('index2', views.index, name='index'),
]

