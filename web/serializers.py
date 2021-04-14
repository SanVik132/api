from rest_framework import serializers
from web.models import * 
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny



class Msignin(serializers.Serializer):
    mobile = serializers.CharField(max_length=10,min_length=10)

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','email', 'mobile','password')

class OTPLoginSerializer(serializers.Serializer):
    mobile = serializers.CharField(required=True,max_length=10, min_length=10)
    otp = serializers.CharField(required=True)



class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key',)

class OTPLoginSerializer(serializers.Serializer):
    mobile = serializers.CharField(required=True,  max_length=10, min_length=10)
    otp = serializers.CharField(required=True)

class UserDetailsSerializer(serializers.ModelSerializer):
    @staticmethod
    def validate_password(password: str) -> str:
        return make_password(password)
    class Meta:
        model = User
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    admin = UserDetailsSerializer(read_only=True)
    class Meta:
        model = Student
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    admin = UserDetailsSerializer(read_only=True)
    class Meta:
        model = Teacher
        fields = '__all__'
