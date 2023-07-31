from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'rams_app/pages/index.html')

def overview(request):
    return render(request, 'rams_app/pages/overview.html')