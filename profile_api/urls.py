from django import urls
from django.urls import path, include
from django.urls.resolvers import URLPattern
from rest_framework.routers import DefaultRouter
from profile_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('helloapi', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()), 
    path('', include(router.urls))
]