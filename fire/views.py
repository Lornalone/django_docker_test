from django.shortcuts import render

# Create your views here.

def index(request):
    
    context = {
        "app_name": "JOOMLA"
    }
    return render(request, "index.html", context=context)
