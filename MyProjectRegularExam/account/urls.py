from django.urls import path

from MyProjectRegularExam.account.views import create_profile, catalogue, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('profile/create/', create_profile, name="create_profile"),
    path('car/catalogue/',catalogue,name='catalogue')
]