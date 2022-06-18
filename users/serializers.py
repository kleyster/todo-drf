from rest_framework import serializers
from .models import CustomUser

class UserRegistrationSerializer(serializers.Serializer):
    
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True,required=True)



    def validate(self,data):
        if not data.get('email'):
            raise serializers.ValidationError({"error" : "Email not found"})
        if CustomUser.objects.filter(email=data.get('email')).exists():
            raise serializers.ValidationError({"error":"Email already exists"})
        return data

    def create(self,data):
        instance = CustomUser.objects.create(**data)
        instance.set_password(data.get("password"))
        instance.save()
        return instance
    


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ("email",'first_name', 'last_name', 'password',)

        extra_kwargs = {
            "first_name": {"required": False},
            "email": {"read_only": True},
            "last_name": {"required": False},
            "password": {"required": True,"write_only": True},
        }

    
    # def update(self,instance,validated_data):
        