from django.urls import path
from django.urls.resolvers import URLPattern
from profile_api import views

urlpatterns = [
    path('helloapi', views.HelloApiView.as_view())
]