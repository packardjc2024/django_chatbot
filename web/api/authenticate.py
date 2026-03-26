# permissions.py
from rest_framework.permissions import BasePermission
from django.conf import settings


API_KEY = settings.REST_KEY # Store in env vars in production!

class HasAPIKey(BasePermission):
    """
    Allows access only if a valid API key is provided in headers.
    """
    def has_permission(self, request, view):
        return request.headers.get("X-API-KEY") == API_KEY