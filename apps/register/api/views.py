from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status

# Create your views here.
@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.save()
        
        user_data = UserSerializer(user).data
        
        return Response({
            "message": "usuario registrado exitosamente",
            "user": user_data
        }, status=status.HTTP_201_CREATED)
        
    return Response({
        "message": "Error en el registro",
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)