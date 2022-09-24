from django.urls import path
from . views import index, loginPage, registerPage, dashboard, logoutPage

urlpatterns = [
    path('', index, name="home"),
    path('login/', loginPage, name="login-user"),
    path('register/', registerPage, name="register-user"),
    path('dashboard/', dashboard, name="dashboard"),
    path('logout/', logoutPage , name="logout-user"),
]