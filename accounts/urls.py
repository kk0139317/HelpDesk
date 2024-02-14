from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path("register/", views.register, name="register"),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.register, name='signup'),
    # path('register/', views.register, name='register'),
    path('verify_otp/<int:user_id>/', views.verify_otp, name='verify_otp'),
]
