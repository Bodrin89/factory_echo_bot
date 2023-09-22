from django.urls import path

from apps.user.views import LoginView, LogoutView, SignUpView, TokenUserBot

urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('token', TokenUserBot.as_view(), name='token-user'),
]
