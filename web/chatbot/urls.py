from django.urls import path
from . import views
from account.decorators import conditional_login_required


app_name = 'chatbot'

urlpatterns = [
    path('', conditional_login_required(views.index), name='index'),
    path('clear_history/', conditional_login_required(views.clear_history), name='clear_history'),
]