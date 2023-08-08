from django.contrib.auth import authenticate
# from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Account


class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    def get_role(self, obj):
        try:
            role = obj.groups.all()[0].name
        except:
            role = None
        return role

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'role')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        User.objects.filter(username=attrs['username'])

        if not user:
            raise serializers.ValidationError('Incorrect username or password.')

        if not user.is_active:
            raise serializers.ValidationError('User is disabled.')

        return {'user': user}


class EditUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_old_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('Old password is not correct')
        return value

    def validate_new_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters')
        return value
# class RegisterationSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     description = serializers.CharField()
#     phone_number = serializers.CharField()
#     email = serializers.EmailField()
#     password = serializers.CharField(
#         style={'input_type': 'password'},
#         write_only=True
#     )
#     password2 = serializers.CharField(
#         style={'input_type': 'password'},
#         write_only=True
#     )
#
#     def validate(self, attrs):
#         user_name = []
#         users = Account.objects.all()
#
#         for u in users:
#             user_name.append(u.username)
#
#         if attrs['username'] in user_name:
#             raise serializers.ValidationError('This username already exist')
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError('Password must match')
#         return attrs
#
#     def create(self, validated_data):
#         return Account.objects.create(
#             username=validated_data['username'],
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name'],
#             description=validated_data['description'],
#             phone_number=validated_data['phone_number'],
#             email=validated_data['email'],
#             password=validated_data['password']
#         )
