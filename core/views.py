from django.shortcuts import render

def index(request):
    """
    Render the index page with a floating shapes effect.
    """
    return render(request, 'index.html')