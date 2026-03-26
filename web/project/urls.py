"""
Project level urls. Imports url pages from each app and includes the built in
admin urls page.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('system_check/', include('system_check.urls')),
    path('', include('home_page.urls')),
]

# Conditionally use account based on LOGIN_REQUIRED
if settings.USE_ACCOUNT:
    urlpatterns.append(path('account/', include('account.urls')))

if settings.USE_API:
    urlpatterns.append(path('api/', include('api.urls')))

if settings.USE_EDITOR:
    urlpatterns.append(path('editor/', include('editor.urls')))

if settings.USE_ADMIN:
    urlpatterns.append(path('admin/', admin.site.urls))

if settings.USE_CHATBOT:
    urlpatterns.append(path('chatbot/', include('chatbot.urls')))

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
