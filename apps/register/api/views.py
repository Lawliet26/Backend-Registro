from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status
from ..models import User
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.save()
        
        #Generar tokens JWT automaticamente
        refresh = RefreshToken.for_user(user)
        
        user_data = UserSerializer(user).data
        
        return Response({
            "message": "usuario registrado exitosamente",
            "user": user_data,
            "tokens": {
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }
        }, status=status.HTTP_201_CREATED)
        
    return Response({
        "message": "Error en el registro",
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    try:
        user= User.objects.get(email=email)
        
        # Validaciones
        if not user.activo or not user.terminos or not user.check_password(password):
            return Response({
                'message': 'Credenciales incorrectas o usuario inactivo'
            })
        
        # Generar Tokens
        refresh = RefreshToken.for_user(user)
        
        return Response({
            "message": "Login exitoso",
            "user":{
                "id":user.id,
                "email": user.email,
                "nombre": user.nombre,
                "apellido": user.apellido,
                "rol": user.rol
            },
            "tokens":{
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }
        }, status=status.HTTP_200_OK)
    
    except User.DoesNotExist:
        return Response({
            "message": "Credenciales incorrectas"
        }, status=status.HTTP_401_UNAUTHORIZED)