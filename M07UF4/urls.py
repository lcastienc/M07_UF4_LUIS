from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index_one'),
    path('teachers', views.teachers,name='teachers'),
    path('students', views.students, name='students'),
    path('student/<str:pk>/', views.student, name='student'),
    path('teacher/<str:pk>/', views.teacher, name='teacher')

    # path('index2', views.index, name='index'),3
]

