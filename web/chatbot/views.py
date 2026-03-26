from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from google import genai
from google.genai import errors
from django.conf import settings


client = genai.Client(api_key=settings.GOOGLE_KEY)


# Create your views here.
def index(request):
    model = 'gemini-2.5-flash-lite'
    if 'chat_history' not in request.session:
        request.session['chat_history'] = []
    
    if request.method == 'POST':
        # Get and add the prompt
        prompt = request.POST.get('prompt')
        
        # Get the response
        history = request.session['chat_history']
        try:
            chat = client.chats.create(model=model, history=history)
            response = chat.send_message(prompt)
        except errors.APIError as e:
            return  HttpResponse('Model free tier quota exceeded...')

        # Update the history
        history.append({'role': 'user', 'parts': [{'text': prompt}]})
        history.append({'role': 'model', 'parts': [{'text': response.text}]})
        request.session['chat_history'] = history

    context = {'chat_history': request.session['chat_history']}
    return render(request, 'chatbot/index.html', context)


def clear_history(request):
    request.session.clear()
    return redirect('chatbot:index')