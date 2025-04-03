from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='rentCar_index'),
    path('add_car/',views.add_car, name='add_car'),
    path('auth/', views.CustomLoginView.as_view(), name='auth'),
    path('logout/', LogoutView.as_view(next_page='auth'), name="logout"),
    path('register', views.RegisterPage.as_view(), name='register'),
    path('filter/', views.filter, name='filter'),
    path('nothification/', views.nothification, name='nothification'),
    path('settings/', views.settings, name='settings'),
    path('rent_car', views.rent_car, name='cars'),
    path('user', views.user, name='user'),
    path('car', views.car, name='car'),
    
]