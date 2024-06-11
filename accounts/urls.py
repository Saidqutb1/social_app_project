from django.urls import path
from .views import SignUpView, CustomLoginView, edit_profile, profile
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/', profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]