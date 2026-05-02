from django.urls import path
from .views import signup_view, login_view, logout_view, dashboard, dashboard_api

urlpatterns = [
    path('', login_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('api/dashboard/', dashboard_api, name='dashboard_api'),
]