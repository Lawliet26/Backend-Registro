from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from ..models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, validators = [validate_password])
    password_confirm = serializers.CharField(write_only= True)
    
    class Meta:
        model = User
        fields = [
            'password', 'password_confirm', 'rol', 'nombre', 
            'apellido', 'email', 'identificacion', 'terminos'
        ] 
        extra_kwargs = {
            "password" : {"write_only":True},
            "email": {"required" : True},
            "terminos": {"required": True}
        }
        
    def validate(self, attrs):
        if attrs["password"] != attrs["password_confirm"]:
            raise serializers.ValidationError("Las constraseñas no coinciden")
        
        if not attrs.get("terminos"):
            raise serializers.ValidationError("Debe aceptar los terminos y condicioes")
        
        attrs.pop("password_confirm")
        return attrs
        
    def create(self, validated_data):
        password = validated_data.pop("password")
        
        username = validated_data["email"].split("@")[0]
        
        counter = 1
        original_username = username
        while User.objects.filter(username=username).exists():
            username = f"{original_username}{counter}"
            counter += 1
        
        user = User.objects.create_user(
            username=username,
            password = password,
            **validated_data
        )
        return user
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'rol', 'nombre', 'apellido', 
            'email', 'identificacion', 'fecha_registro', 'activo'
        ]
        read_only_fields = ["id","fecha_registro"]