from django.urls import path
from .views import health_check

app_name = 'system_check'

urlpatterns = [
    path('health/', health_check, name='health-check'),
]