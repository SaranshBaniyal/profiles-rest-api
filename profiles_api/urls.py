from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router =  DefaultRouter() #for viewset
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset') #for viewset

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()), #for api views
    path('', include(router.urls)), #for viewset
]

#we use routers for viewset