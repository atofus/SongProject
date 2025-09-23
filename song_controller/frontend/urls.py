from django.urls import path # added include function.
from .views import index #the method we created in views.py

urlpatterns = [
    path('', index), # Now we'll render the index template when we have a blank path. That will kinda be our homepage
    path('join', index), # For join page
    path('create', index) # For create room page
]