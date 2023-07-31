from django.urls import path
from rams_app.views import index, overview


urlpatterns = [
    path('', index, name='index'),
    path('overview/', overview, name='overview'),
    ]