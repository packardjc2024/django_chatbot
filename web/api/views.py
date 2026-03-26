from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Credential
from django.forms.models import model_to_dict
from django.shortcuts import render, redirect
from cryptography.fernet import Fernet
from django.http import JsonResponse
from account.decorators import conditional_login_required
from django.db import IntegrityError

###############################################################################
# Functions
###############################################################################
def generate_key() -> str:
    return Fernet.generate_key().decode('utf-8')

def encrypt_secret(key: str, secret: str) -> str:
    cipher = Fernet(key.encode('utf-8'))
    return cipher.encrypt(secret.encode('utf-8')).decode('utf-8')

def decrypt_secret(key: str, secret: str) -> str:
    cipher = Fernet(key.encode('utf-8'))
    return cipher.decrypt(secret.encode('utf-8')).decode('utf-8')

###############################################################################
# Views
###############################################################################

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_credentials(request):
    """
    """
    data = request.data
    if request.user.is_authenticated:
        try:
            credential = Credential.objects.get(user=request.user, application=data['app'])
            encrypted_pw = credential.password
            return Response({'encrypted_pw': encrypted_pw})
        except Credential.DoesNotExist:
            return Response({'Error': 'No credential found.'})
    else:
        return Response({'Error': 'No credential found.'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_credentials(request):
    """
    """ 
    data = request.data
    app = data['app']
    pw = data['pw']
    key = generate_key()
    encrypted_pw = encrypt_secret(key, pw)
    # Update existing or create new credential
    try:
        credential = Credential.objects.create(
            user=request.user,
            application=app,
            password=encrypted_pw,
        )
        message = 'Credentials successfully added. Save your key.'
        credential.save()
    except IntegrityError:
        key = None
        message = 'You cannot have multiple passwords for the same app. Overwrite it'
    return Response({'message': message, 'key': key})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_credentials(request):
    """
    """
    pass