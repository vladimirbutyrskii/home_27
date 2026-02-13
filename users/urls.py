from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateView, email_verification  # , email_verification, reset_password
# from django.contrib.auth import views as authViews

from users.views import logout_view

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', logout_view, name='logout'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path("email-confirm/<str:token>/", email_verification, name='email-confirm'),
    # path("reset_password/", reset_password, name='reset_password'),
]




    #  path('exit/', authViews.LogoutView.as_view(next_page='Здесь ссылка перенаправления'), name='exit')
