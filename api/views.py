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



# ==============> MONGO views <=======================
class CustomPostView(views.APIView):
    def get(self,request):
        param_name=request.query_params['username']

        db=client['socialmedia']
        collection=db['user_posts']
        dataList=list(collection.find({'user':param_name}))
        parsedData=json.loads(json_util.dumps(dataList))
        return Response(status=200, data={'data':parsedData})
    
    def post (self, request):
        body=request.data
        # TODO: Handle errors from request data 
        db=client['socialmedia']
        collection=db['user_posts']
        try:
            response=collection.insert_one(body)
        except Exception as error:
            return Response(status=500, data={'success':False, 'message':error, 'response':response})
            
        return Response(status=201, data=response)
        
class CustomRequestView(views.APIView):
    def get (self,request):
        db=client['socialmedia']
        collection=db['user_requests']
        dataList=list(collection.find())
        parsedData=json.loads(json_util.dumps(dataList))
        return Response(status=200, data={'data':parsedData})

    def post (self,request):
        body=request.data
        # TODO: Handle errors from request data 
        db=client['socialmedia']
        collection=db['user_requests']

        try:
            user=collection.find_one({'user':body['user']})
            userData= json.loads(json_util.dumps(user))
            if user:
                reqfrom=userData['reqFrom']
                reqTo=userData['sentTo']
                try:
                    if body['reqFrom']:
                        reqfrom.append(body['reqFrom'])
                except Exception as e:
                    print(e)
                try:
                    if body['sentTo']:
                        reqTo.append(body['sentTo'])
                except Exception as e:
                    print(e)
                
                updated_data={'reqFrom':reqfrom, 'sentTo':reqTo}
                collection.update_one({'user':body['user']},{'$set':updated_data})

        except Exception as error:
            return Response(status=500, data={'success':False, 'message':error})
            
        return Response(status=201, data={'message':'Actualizado correctamente'})

class FriendsView(views.APIView):
    def get (self, request):
        params=request.query_params
        db=client['socialmedia']
        collection=db['user_friends']
        dataList=list(collection.find({'user':params['username']}))
        parsedData=json.loads(json_util.dumps(dataList))
        return Response(status=200, data={'data':parsedData})
    def post (self,request):
        body=request.data
        # TODO: Handle errors from request data 
        db=client['socialmedia']
        collection=db['user_friends']

        try:
            user=collection.find_one({'user':body['user']})
            userData= json.loads(json_util.dumps(user))
            if user:
                friends=userData['friends']
                friends.append(body['friend'])

                updated_data={'friends':friends}
                collection.update_one({'user':body['user']},{'$set':updated_data})

        except Exception as error:
            return Response(status=500, data={'success':False, 'message':error})
            
        return Response(status=201, data={'message':'Actualizado correctamente'})
        
