from django.urls import path   #urls=path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
]