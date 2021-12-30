from django.shortcuts import render
from xpense_users.models.users import User
from rest_framework.views import APIView
from xpense_users.serializers.user_serializer import UserSerializer

# Create your views here.
class RegistrationView(APIView):

    serializer_class = UserSerializer
    
    def get(self, request):
        pass
    
    def put(self, request):
        pass

    def post(self, request):
        pass
    
    def delete(self, request):
        pass