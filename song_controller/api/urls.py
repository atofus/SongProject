from django.urls import path, include # added include function.
from .views import RoomView


# After coming from the song_controller/urls.py section, it'll go here potentially, and this is where we call the functions!
urlpatterns = [
    # path('', main) # If we get any url, we'll go over to the main function that's in views.py. So, instead of pointing at another file, we could point them to the function inside of view.

    path('room', RoomView.as_view()), # As view means to take the class and give me the view for it.
]