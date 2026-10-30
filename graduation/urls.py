from django.urls import path
from .views import home_view

urlpatterns = [
    # Maps the root URL of your app to the home landing page view
    path('', home_view, name='home'),
]