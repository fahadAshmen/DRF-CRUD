from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from . serializers import CreateUserSerializer, UpdateUserSerializer, LoginSerializer
from rest_framework.permissions import AllowAny
from . models import User
from knox import views as knox_views
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework import status
from hospital.permissions import IsOwnerOnly
from rest_framework import permissions

class CreateUserAPI(CreateAPIView, ListAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

class UpdateUserAPI(UpdateAPIView):
    serializer_class = UpdateUserSerializer
    queryset = User.objects.all()
    permission_classes = (IsOwnerOnly, permissions.IsAuthenticated)

class LoginUserAPI(knox_views.LoginView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, format=None):        

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request,user)

            response =super().post(request, format=None)
        else:
            return Response({'errors': serializer.errors}, status.HTTP_400_BAD_REQUEST)

        return Response(response.data, status=status.HTTP_200_OK)






