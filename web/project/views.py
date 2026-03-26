from django.shortcuts import render
import json
from django.conf import settings
from pathlib import Path


def index(request):
    context = {}
    return render(request, 'base.html', context)