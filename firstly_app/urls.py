from django.urls import path
from . import views

urlpatterns = [
    path("<int:num1>/",views.course_number , name="numm"),
    path("<str:item>/", views.course, name="course"),
    path('firstly_app', views.index, name='index')
]


