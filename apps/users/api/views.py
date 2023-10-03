from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.users.models import User
from apps.users.api.serializers import UserSerializer, UserRegisterSerializer, UserUpdateSerializer


class RegisterAPIView(APIView):
    
    User = get_user_model()
    
    def post(self, request):
        # Inside "request.data" is where we have all the user information
        serializer = UserRegisterSerializer(data=request.data)

        # Validate that the serializer is valid
        if serializer.is_valid(raise_exception=True):
            # Set the "username" field to the value of the email
            username = serializer.validated_data['email']
            serializer.validated_data['username'] = username
            
            # Save user
            user = User.objects.create_user(**serializer.validated_data)
            
            return Response(serializer.data)
        # If it is not valid, return a 404 error
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserAPIView(APIView):
    # To access this view you must be authenticated
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # In "request.user" we have all the user data (email, firstname, lastname)
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
    def put(self, request):
        user = User.objects.get(id=request.user.id)
        # We pass the current data of the user "user" and the new data "request.data"
        serializer = UserUpdateSerializer(user, request.data)
        
         # Validate that the serializer is valid
        if serializer.is_valid(raise_exception=True):
           serializer.save()
           return Response(serializer.data)
        # If it is not valid, return a 404 error
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        