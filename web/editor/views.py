from django.shortcuts import render, redirect
from pathlib import Path
from django.conf import settings
import json
from django.http import JsonResponse
from project.generate_css import generate_css_file


###############################################################################
# Constants
###############################################################################
CONFIG_PATH = settings.CONFIG_PATH

SECTIONS = [
    'general',
    'navbar',
    'footer',
    'api',
    'email',
]

FORMS = []
for section in SECTIONS:
    FORMS.append({
        'value': section,
        'display': section.title().replace('_', ' '),
        'url': f'editor:{section}',
    }) 

def read_config():
    with open(CONFIG_PATH, 'r') as file:
        data = json.load(file)
    return data

def write_config(data):
    with open(CONFIG_PATH, 'w') as file:
        json.dump(data, file, indent=4)
    generate_css_file()

###############################################################################
# Views
###############################################################################

def index(request):
    context = {'forms': FORMS} 
    if request.method == 'GET':
        return render(request, 'editor/index.html', context)


def navbar(request):
    context = {'forms': FORMS} 
    data = read_config()
    if request.method == 'GET':
        # Preload the current settings
        context['navbar'] = {
            'style': data['navbar']['style'],
            'fixed': data['navbar']['fixed'],
            'use_navbar': data['navbar']['use_navbar'],
            'height': int(data['navbar']['height']),
            'glass': data['navbar']['glass'],
            'margin_top': data['navbar']['margin_top']
        }
        return render(request, 'editor/navbar_form.html', context)
    if request.method == 'POST':
        print(request.POST.get('navbar-height'))
        data['navbar']['style'] = request.POST.get('navbar-style')
        data['navbar']['fixed'] = True if request.POST.get('navbar-fixed') == 'true' else False
        data['navbar']['use_navbar'] = True if request.POST.get('use-navbar') == 'true' else False
        data['navbar']['glass'] = True if request.POST.get('glass') == 'true' else False
        data['navbar']['height'] = str(request.POST.get('navbar-height'))
        data['navbar']['margin_top'] = str(request.POST.get('navbar-margin-top'))
        write_config(data)
    return redirect('editor:index')


def general(request):
    context = {'forms': FORMS} 
    data = read_config()
    if request.method == 'GET':
        # Preload the current settings
        context['general'] = {
            'site_title': data['general']['site_title'],
            'primary_color': data['general']['primary_color'],
            'navbar_color': data['general']['navbar_color'],
        }
        return render(request, 'editor/general_form.html', context)
    if request.method == 'POST':
        data['general']['site_title'] = request.POST.get('site-title')
        data['general']['primary_color'] = request.POST.get('primary-color')
        data['general']['navbar_color'] = request.POST.get('navbar-color')
        write_config(data)
        return redirect('editor:index')


def api(request):
    context = {'forms': FORMS}
    data = read_config()
    if request.method == 'GET':
        context['api'] = {
            'use_api': data['apps']['use_api'],
        }
        return render(request, 'editor/api_form.html', context)
    if request.method == 'POST':
        data['apps']['use_api'] = True if request.POST.get('use-api') == 'true' else False
        write_config(data)
        return redirect('editor:index')


def email(request):
    context = {'forms': FORMS}
    data = read_config()
    if request.method == 'GET':
        context['email'] = {
            'use_email': data['apps']['use_email'],
        }
        return render(request, 'editor/email_form.html', context)
    if request.method == 'POST':
        data['email']['use_email'] = True if request.POST.get('use-email') == 'true' else False
        write_config(data)
        return redirect('editor:index')
    

def footer(request):
    context = {'forms': FORMS} 
    data = read_config()
    if request.method == 'GET':
        # Preload the current settings
        context['footer'] = {
            'height': data['footer']['height'],
            'background_color': data['footer']['background_color']
        }
        return render(request, 'editor/footer_form.html', context)
    if request.method == 'POST':
        print(request.POST.get('navbar-height'))
        data['footer']['height'] = request.POST.get('footer-height')
        data['footer']['background_color'] = request.POST.get('footer-background-color')
        write_config(data)
    return redirect('editor:index')
    
