from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('forecasts/', views.forecasts, name='forecasts'),
    path('metrics/', views.metrics, name='metrics'),
    path('dashboard/', views.forecast_dashboard, name='forecast_dashboard'),
]

