from rest_framework import serializers
from .models import Profile,Post
class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'

class postSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'