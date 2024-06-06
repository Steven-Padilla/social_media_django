from rest_framework import viewsets, views
from rest_framework.response import Response
from .serializer import profileSerializer, postSerializer
from .models import Post, Profile
from .utils import client
from bson import json_util
import json
# Create your views here.
class ProfileView(viewsets.ModelViewSet):
    serializer_class=profileSerializer
    queryset=Profile.objects.all()

class PostView(viewsets.ModelViewSet):
    serializer_class=postSerializer
    queryset=Post.objects.all()

class CustomPostView(views.APIView):
    def get(self,request):
        db=client['socialmedia']
        collection=db['user_posts']
        dataList=list(collection.find())
        parsedData=json.loads(json_util.dumps(dataList))
        print(parsedData)
        return Response(status=200, data={'data':parsedData})
    
    def post (self, request):
        body=request.data

        print(body)
        return Response(status=200, data=body)
        