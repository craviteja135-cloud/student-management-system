from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('students/', views.student_list, name="student_list"),
    path('delete_student/', views.delete_latest_student, name="delete_latest_student"),
    path('api/students/', views.student_api, name='student_api'),
    path('api/students/<int:id>/', views.students_detail_api,name="students_detail_api"),
]