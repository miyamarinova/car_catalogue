from django.urls import path

from MyProjectRegularExam.account.views import create_profile, catalogue, IndexView,profile_details_page,edit_profile,delete_profile

urlpatterns = [
    path('', IndexView.as_view(), name="index"),

    path('profile/create/', create_profile, name="create_profile"),
    path('car/catalogue/',catalogue,name='catalogue'),
    path('profile/detail/',profile_details_page, name="detail_profile"),
    path('profile/edit/', edit_profile, name='edit_profile' ),
    path('profile/delete/',delete_profile, name='delete_profile' )
]