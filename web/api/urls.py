from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = 'api'

urlpatterns = [
    path('request_token/', TokenObtainPairView.as_view(), name='request_token'),
    path('refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
    path('get_credentials/', views.get_credentials, name='get_credentials'),
    path('add_credentials/', views.add_credentials, name='add_credentials'),
    path('update_credentials/', views.update_credentials, name='update_credentials')
]