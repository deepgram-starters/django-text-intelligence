from django.urls import path
from . import views
urlpatterns = [
    path('text-intelligence/analyze', views.analyze, name='analyze'),
    path('api/metadata', views.metadata, name='metadata'),
]
