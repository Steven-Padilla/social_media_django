from django.urls import include, path
from rest_framework import routers
from api import views



router= routers.DefaultRouter()
router.register(r'profile', views.ProfileView, 'profile')
router.register(r'post', views.PostView, 'post')

urlpatterns=[
    path('/postmongo', views.CustomPostView.as_view()),
    path("/", include(router.urls))
]