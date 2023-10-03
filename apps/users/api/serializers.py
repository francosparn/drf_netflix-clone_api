from rest_framework.serializers import ModelSerializer

from apps.users.models import User


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'password']
        
    def create(self, validated_data):
        # Extract password so that it is not stored in plain text
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        
        # If a password was provided, the "set_password" method is called to store the password securely
        if password is not None:
            instance.set_password(password)
        # Save the user instance to the database    
        instance.save()
        # Return newly created instance
        return instance


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name']
        
        
class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']