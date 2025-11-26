from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True , min_length=8 , max_length=60)
    password2 = serializers.CharField(write_only=True , min_length=8 , max_length=60)
    class Meta:
        model = CustomUser
        fields = ['username','first_name', 'last_name' ,'email','password','password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Passwordlar bir xil emas. Qayta kiriting!')
        return data

    def save(self, validated_data):
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username','first_name', 'last_name' ,'email','role']