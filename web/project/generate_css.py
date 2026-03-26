from pathlib import Path
import json
from django.conf import settings

def generate_css_file():
    # Deal with filepaths.
    themes_prod_filepath = Path.joinpath(settings.BASE_DIR, 'staticfiles', 'themes.css')
    themes_dev_filepath = Path.joinpath(settings.BASE_DIR, 'static', 'themes.css')
    config_path = settings.CONFIG_PATH
    css = {}

    # Read the config file
    with open(config_path, 'r') as file:
        data = json.load(file)

    # General
    css['--primary-color'] = data['general']['primary_color']
    if data['navbar']['use_navbar'] or data['footer']['use_footer']:
        if data['navbar']['height']:
            navbar_height = data['navbar']['height']
        if data['footer']['height']:
            footer_height = data['footer']['height']
        css['--main-section-height'] = f'calc(100vh - {navbar_height}px - {footer_height}px)'
    else:
        css['--main-section-height'] = '100vh'

    # Navbar:
    if data['navbar']['use_navbar']:
        css['--navbar-height'] = f"{data['navbar']['height']}px"
        if data['navbar']['fixed']:
            css['--navbar-fixed'] = 'fixed'
            css['--main-section-margin-top'] = f"{int(data['navbar']['height']) + int(data['navbar']['margin_top'])}px"
        css['--navbar-width'] = '100%'
        if data['navbar']['style'] == 'rounded':
            css['--navbar-border-radius'] = '20px'
            css['--navbar-width'] = '95%'
            css['--navbar-margin-top'] = data['navbar']['margin_top'] + 'px'
        if not data['navbar']['glass']:
            css['--navbar-background-color'] = data['general']['navbar_color']

    # Footer:
    if data['footer']['use_footer']:
        css['--footer-background-color'] = data['footer']['background_color']
        css['--footer-height'] = data['footer']['height'] + 'px'
    

    # Create the file content
    css_string = ''
    for key, value in css.items():
        css_string += f'\t{key}: {value} !important;\n'
    css_content = f':root {{\n{css_string}\n}}'

    # Write the files. 
    
    with open(themes_prod_filepath, 'w') as file:
        file.write(css_content.strip())
    if settings.DEBUG:
        with open(themes_dev_filepath, 'w') as file:
            file.write(css_content.strip())
