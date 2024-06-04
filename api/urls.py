from django.urls import include, path
from rest_framework import routers
from api import views



router= routers.DefaultRouter()
router.register(r'profile', views.ProfileView, 'profile')

urlpatterns=[
    path("api/v1/", include(router.urls))
]