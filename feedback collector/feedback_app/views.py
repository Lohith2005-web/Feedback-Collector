from django.shortcuts import render, redirect
import urllib.request
import json
from django.http import HttpResponse

NODE_URL = 'http://localhost:3000/feedback'

def index(request):
    return render(request, 'feedback_app/index.html')

def submit_feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        data = json.dumps({
            'name': name,
            'email': email,
            'message': message
        }).encode('utf-8')

        req = urllib.request.Request(NODE_URL, data=data, headers={'Content-Type': 'application/json'})
        try:
            urllib.request.urlopen(req)
        except Exception as e:
            return HttpResponse(f"Error connecting to Node.js backend: {e}")

        return redirect('feedbacks')
    return redirect('index')

def show_feedbacks(request):
    try:
        with urllib.request.urlopen(NODE_URL) as response:
            data = json.loads(response.read().decode('utf-8'))
    except Exception as e:
        data = []
    
    return render(request, 'feedback_app/feedbacks.html', {'feedbacks': data})
