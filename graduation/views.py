from django.shortcuts import render

def home_view(request):
    """
    Renders the modern welcoming landing page for Theophilus Manthi Kitolo's Grade 9 Graduation.
    """
    return render(request, 'home.html')