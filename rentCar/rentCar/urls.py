from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('add_car/',views.add_car, name='add_car'),
    path('auth/', views.CustomLoginView.as_view(), name='auth'),
    path('logout/', LogoutView.as_view(next_page='auth'), name="logout"),
    path('register', views.RegisterPage.as_view(), name='register'),
    path('filter/', views.filter, name='filter'),
    path('nothification/', views.nothification, name='nothification'),
    path('settings/', views.settings, name='settings'),
    path('', views.rent_car, name='cars'),
    path('user', views.user, name='user'),
    
    path('car_detail/<int:pk>/', views.car_detail, name='car_detail'),
    
]