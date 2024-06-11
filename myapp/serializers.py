from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a new user.
    """
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}
    
    def create(self, validated_data):
        """
        Create and return a new user with an encrypted password.
        """
        user = User.objects.create_user(**validated_data)
        return user


class AuthSerializer(serializers.Serializer):
    """
    Serializer for user authentication.
    """
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """
        Validate and authenticate the user.
        """
        username = attrs.get('username')
        password = attrs.get('password')
        
        user = authenticate(
            username=username,
            password=password
        )
        
        if not user:
            msg = 'Unable to authenticate with provided credentials'
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs
