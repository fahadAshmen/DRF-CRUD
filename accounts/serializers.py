from rest_framework import serializers
from . models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','username','first_name','last_name','role']

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','username','first_name','last_name','roles','password']
        extra_kwargs ={
            'password' : {'required': True}
        }

    def validate(self,attrs):
        email = attrs.get('email','').strip().lower()
        username = attrs.get('username', '').lower()

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User with this email id exists')
        
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('Username already taken')
        
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username','first_name','last_name','password','roles')

    def update(self, instance, validated_data):    

        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        instance = super().update(instance, validated_data)
        return instance

class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type':'password'}, trim_whitespace=False)

    def validate(self, attrs):

        email = attrs.get('email').lower()
        password = attrs.get('password')

        if not email or not password:
            raise serializers.ValidationError('Email and Password are required')
        
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email does not exists')
        
        user = authenticate(email=email,password=password)

        if not user:
            raise serializers.ValidationError("Wrong Credentials")
        
        attrs['user']=user
        return attrs


        

