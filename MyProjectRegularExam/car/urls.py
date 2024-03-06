from django.urls import path

from MyProjectRegularExam.car.views import create_car, DetailCarView, EditCarView, DeleteCarViews

urlpatterns = [
    path('create/', create_car, name='create_car'),
    path('detail/<int:pk>/', DetailCarView.as_view(), name="detail_car"),
    path('edit/<int:pk>/', EditCarView.as_view(), name="edit_car"),
    path('delete/<int:pk>/', DeleteCarViews.as_view(), name="delete_car")
]