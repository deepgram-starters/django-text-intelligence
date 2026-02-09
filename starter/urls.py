from django.urls import path
from . import views
urlpatterns = [
    path('', views.serve_index, name='index'),
    path('api/session', views.get_session, name='session'),
    path('api/text-intelligence', views.analyze, name='analyze'),
    path('api/metadata', views.metadata, name='metadata'),
]
