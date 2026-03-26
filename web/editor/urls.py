from django.urls import path
from . import views
from account.decorators import conditional_login_required


app_name = 'editor'

urlpatterns = [
    path('', conditional_login_required(views.index), name='index'),
    path('navbar/', conditional_login_required(views.navbar), name='navbar'),
    path('footer/', conditional_login_required(views.footer), name='footer'),
    path('general/', conditional_login_required(views.general), name='general'),
    path('api/', conditional_login_required(views.api), name='api'),
    path('email/', conditional_login_required(views.email), name='email'),
]