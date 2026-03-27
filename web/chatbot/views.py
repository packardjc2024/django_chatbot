from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from google import genai
from google.genai import errors, types
from django.conf import settings


client = genai.Client(api_key=settings.GOOGLE_KEY)

system_options = {
    'concise': 'You are a concise assistant.',
    'formal': 'You are a very formal assistant.',
}

free_tier_models = [
    'gemma-3-1b-it',
    'gemma-3-4b-it',
    'gemma-3-12b-it',
    'gemma-3-27b-it',
    'gemma-3n-e4b-it',
    'gemma-3n-e2b-it',
    'gemini-2.5-flash-lite',
]

def format_gemma_response(response):
    return response.replace('**', '\n')


###############################################################################
# Views 
###############################################################################


# Create your views here.
def index(request):
    model = 'gemini-2.5-flash-lite'
    if 'chat_history' not in request.session:
        request.session['chat_history'] = []
    if 'system_setting' not in request.session:
        request.session['system_setting'] = 'concise'
    
    # Print free tier models:
    # for free_model in client.models.list():
    #     print(free_model.name)

    print(request.session['system_setting'])
    
    if request.method == 'POST':
        # Get and add the prompt
        prompt = request.POST.get('prompt')
        
        # Get the response 
        history = []
        for msg in request.session['chat_history']:
            if msg['role'] == 'user':
                history.append(types.UserMessage(content=msg['content']))
            else:
                history.append(types.AssistantMessage(content=msg['content']))
        try:
            chat = client.chats.create(
                model=model, 
                history=history,
                config=types.GenerateContentConfig(
                    system_instruction=system_options[request.session['system_setting']],
                ),
            )
            response = chat.send_message(prompt)
        except errors.APIError as e:
            return  HttpResponse('Model free tier quota exceeded...')

        # Update the history
        request.session['chat_history'].append({'role': 'user', 'content': prompt})
        request.session['chat_history'].append({'role': 'assistant', 'content': format_gemma_response(response.text)})

    context = {
        'chat_history': request.session['chat_history'],
        'system_setting': request.session['system_setting']
    }
    return render(request, 'chatbot/index.html', context)


def clear_history(request):
    del request.session['chat_history']
    return redirect('chatbot:index')


def edit_model_system(request):
    if request.method == 'POST':
        new_setting = request.POST.get('system_setting')
        if new_setting not in system_options:
            return HttpResponse('Now a valid system option')
        else:
            request.session['system_setting'] = new_setting
    return redirect('chatbot:index')