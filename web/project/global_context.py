"""
This module sets the variables that can be used in any views context dictionary
for rendering templates, including base.html
"""


from datetime import datetime
from django.conf import settings
from dotenv import load_dotenv
import os
from pathlib import Path
from django.templatetags.static import static
import json


def add_global_context(request):
    """
    Adds a global context for use among all templates, especially base.html.
    """
    # Load Secrets
    SECRETS_PATH = Path.joinpath(settings.BASE_DIR, '.env')
    load_dotenv(SECRETS_PATH)

    # Load config data
    CONFIG_PATH = settings.CONFIG_PATH
    with open(CONFIG_PATH, 'r') as file:
        config_data = json.load(file)

    # Process config data
    page_links = []

    for page in config_data['page_links']:
        if page.lower().strip().replace(' ', '') == 'chatbot' and not config_data['apps']['use_chatbot']:
            pass
        elif page.lower().strip().replace(' ', '') == 'editor' and not config_data['apps']['use_editor']:
            pass
        else:
            page_links.append({
                'display_name': page.title().replace('_', ' '),
                'href': f"{page.lower().replace(' ', '-')}:index",
            })
    
    print(page_links)

    # Return the global context dictionary
    return {
        # General
        'site_title': config_data['general']['site_title'],
        'site_logo_url': static('site_pictures/logo.png'),
        'page_links': page_links,
        # Copyright
        'copyright_name': os.getenv('COPYRIGHT_NAME'),
        'copyright_year': os.getenv('COPYRIGHT_YEAR', datetime.now().year),
        # Accounts
        'use_account': settings.USE_ACCOUNT,
        # Navbar
        'use_navbar': config_data['navbar']['use_navbar'],
        'navbar_glass': config_data['navbar']['glass'],
        'use_contact': config_data['apps']['use_contact'],
        # Footer
        'use_footer': config_data['footer']['use_footer'],
        'attributions': [
            {
                'name': 'test name',
                'text': 'test text',
                'link': 'test link',
            },
        ],
    }