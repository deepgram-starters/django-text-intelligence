from django.urls import path
from . import views
urlpatterns = [
    path('api/text-intelligence', views.analyze, name='analyze'),
    path('api/metadata', views.metadata, name='metadata'),
]
