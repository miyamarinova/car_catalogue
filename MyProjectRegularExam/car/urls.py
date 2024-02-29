from django.urls import path

from MyProjectRegularExam.car.views import create_car

urlpatterns = [
    path('create/', create_car, name='create_car')
]