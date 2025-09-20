"""
URL configuration for song_controller project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # added include function.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')) # If we get the url api/, we'll just send it over to api.urls (api/urls.py folder)
]

"""
How this works:
If the url is 'domain.com/hello', after the slash will be sent to this file and
this file will dispatch the URLs to the correct applications.
EX: 'domain.com/admin/...' would send that url to admin.site.urls file.
"""