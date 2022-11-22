from django.urls import path, include
from .views import SignUpPage,EditProfile,PasswordChange,PwdChanged,ProfilePage,UserProfilePage
#from django.contrib.auth import views as auth_view

urlpatterns = [
    path('register/', SignUpPage.as_view(), name='register' ),
    path('edit-profile/', EditProfile.as_view(), name='edit_profile' ),
    path('password/', PasswordChange.as_view(template_name='registration/password-change.html')),
    path('success-change/', PwdChanged,name='success-change'),
    path('profile-page/', ProfilePage, name='profile-page'),
    path('<int:pk>/profile', UserProfilePage.as_view(), name='user_profile_page'),

]
