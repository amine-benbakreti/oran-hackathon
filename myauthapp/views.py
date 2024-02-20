# myapp/views.py
from rest_framework import status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import generics

@api_view(['POST'])
def signup(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user=serializer.save()
        user=CustomUser.objects.get(username=request.data['username'])
        password = request.data.get('password')
        user.set_password(password)
        user.save()
        token = Token.objects.create(user=user)
        print('amino')
        return Response({"token":token.key,"user":serializer.data})
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    user=get_object_or_404(CustomUser,username=request.data['username'])
    if not user.check_password(request.data['password']):
       return Response(status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = CustomUserSerializer(instance=user)
    return Response({"token":token.key,"user":serializer.data})

class ListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
