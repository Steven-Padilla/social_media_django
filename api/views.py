from rest_framework import viewsets
from .serializer import profileSerializer
from .models import Profile
# Create your views here.
class ProfileView(viewsets.ModelViewSet):
    serializer_class=profileSerializer
    queryset=Profile.objects.all()