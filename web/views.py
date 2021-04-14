from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView,RetrieveUpdateAPIView
from rest_framework import permissions,status,viewsets
from rest_framework.response import Response
from web.serializers import *
from django.conf import settings


def create_token(user):
    token, _ = Token.objects.get_or_create(user=user)
    return token
'''    
class generateKey:
    @staticmethod
    def returnValue(mobile):
        return str(mobile) + str(datetime.date(datetime.now())) + "Some Random Secret Key"
'''


#register view
class register(GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegistrationSerializer
    
    def post(self, request, format=None):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data, context={'request': request})
        self.serializer.is_valid(raise_exception=True)
        mobile = self.request.data["mobile"]
        email = self.request.data["email"]
        first_name = self.request.data["first_name"]
        password = make_password(self.request.data["password"])
        try:
            user = User.objects.get(mobile = mobile, is_active = True)
            data = {
                'mobile': mobile,
                'error':"User already Exists"
            }
            response = Response(data, status=status.HTTP_200_OK)
        except:
            try:
                user= User.objects.get(username = mobile,mobile = mobile,is_active = False).delete()
            except:
                pass
            if mobile.isdigit():
                user = User.objects.create(username = mobile,mobile = mobile,first_name = first_name,email = email,password = password,is_active = False)
                user.save()
                user = OTPs.objects.create(user=user, otp='123456')
                
                data = {
                'mobile': mobile,
                'otp_sent': True,
                }
                response = Response(data, status=status.HTTP_200_OK)
            else:
                data = {
                'mobile': username,
                'otp_sent': False,
                'error': "Please enter phone/mobile number only."
                }
                response = Response(data, status=status.HTTP_400_BAD_REQUEST)
        return response


class ConfirmuserView(GenericAPIView):

    permission_classes = (permissions.AllowAny,)
    serializer_class = OTPLoginSerializer

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data, context={'request': request})
        self.serializer.is_valid(raise_exception=True)

        mobile = self.request.data["mobile"]
        otp = self.request.data["otp"]
        if mobile.isdigit() and otp.isdigit():
            try:
                user = User.objects.get(mobile=mobile)
                try:
                    uotp = OTPs.objects.get(user=user)
                    if int(uotp.otp) == int(otp):
                        user.is_active = True
                        user.save()
                        token = create_token(user)
                        serializer = TokenSerializer(instance=token, context={'request': self.request})
                        token_response = Response(serializer.data, status=status.HTTP_200_OK)
                        response = token_response
                    else:
                        data = {
                            'mobile': mobile,
                            'otp': otp,
                            'error': "OTP Mismatch"
                           }
                        response = Response(data, status=status.HTTP_400_BAD_REQUEST)


                except OTPs.DoesNotExist:
                    data = {
                        'mobile': mobile,
                        'error': "It looks we haven't sent you an OTP. Please try to login again"
                        }
                    response = Response(data, status=status.HTTP_400_BAD_REQUEST)

            except User.DoesNotExist:
                data = {
                    'mobile': mobile,
                    'error': "Awww! You are not registered with us."
                    }
                response = Response(data, status=status.HTTP_400_BAD_REQUEST)

        else:
            data = {
                'mobile': mobile,
                'otp': otp,
                'error': "Invalid Format. Please enter numeric values"
            }
            response = Response(data, status=status.HTTP_400_BAD_REQUEST)
        return response


class Forgotpwdview(GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = Msignin

    def post(self, request, format=None):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data, context={'request': request})
        self.serializer.is_valid(raise_exception=True)
        try:
            mobile = self.request.data["mobile"]
            if mobile.isdigit():
                user = User.objects.get(username=mobile,mobile = mobile)
                try:
                    otp = OTPs.objects.filter(user=user).delete()
                except:
                    pass
                user.save()
                user = OTPs.objects.create(user=user, otp='123456')

            
                data = {
                    'mobile': mobile,
                    'otp_sent': True,
                }
                response = Response(data, status=status.HTTP_200_OK)
            else:
                data = {
                    'mobile': username,
                    'otp_sent': False,
                    'error': "Please enter phone/mobile number only."
                }
                response = Response(data, status=status.HTTP_200_OK)
        except:
            response = Response({"error":"Something went wrong here"}, status=status.HTTP_400_BAD_REQUEST)
        return response

class ConfirmpwdotpView(GenericAPIView):

    permission_classes = (permissions.AllowAny,)
    serializer_class = OTPLoginSerializer

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data, context={'request': request})
        self.serializer.is_valid(raise_exception=True)

        mobile = self.request.data["mobile"]
        otp = self.request.data["otp"]
        if mobile.isdigit() and otp.isdigit():
            try:
                user = User.objects.get(mobile=mobile)
                try:
                    uotp = OTPs.objects.get(user=user)
                    if int(uotp.otp) == int(otp):
                        token = Token.objects.get(user = user)
                        serializer = TokenSerializer(instance=token, context={'request': self.request})
                        token_response = Response(serializer.data, status=status.HTTP_200_OK)
                        response = token_response
                    else:
                        data = {
                            'mobile': mobile,
                            'otp': otp,
                            'error': "OTP Mismatch"
                           }
                        response = Response(data, status=status.HTTP_400_BAD_REQUEST)


                except OTPs.DoesNotExist:
                    data = {
                        'mobile': mobile,
                        'error': "It looks we haven't sent you an OTP. Please try to login again"
                        }
                    response = Response(data, status=status.HTTP_400_BAD_REQUEST)

            except User.DoesNotExist:
                data = {
                    'mobile': mobile,
                    'error': "Awww! You are not registered with us."
                    }
                response = Response(data, status=status.HTTP_400_BAD_REQUEST)

        else:
            data = {
                'mobile': mobile,
                'otp': otp,
                'error': "Invalid Format. Please enter numeric values"
            }
            response = Response(data, status=status.HTTP_400_BAD_REQUEST)
        return response

class NewpasswordView(RetrieveUpdateAPIView):
    serializer_class = UserDetailsSerializer
    permission_classes = (IsAuthenticated,)
    def update(self, request, *args, **kwargs):
        qs = request.user
        self.request = request       
        self.serializer = UserDetailsSerializer(qs,data={'password' : self.request.data['password']} , context={'request': request})
        self.serializer.is_valid(raise_exception=True)
        self.perform_update(self.serializer)
        return Response(self.serializer.data)


class StudentDetailsView(viewsets.ViewSet):
    permission_classes = (permissions.BasePermission,)
    
    def list(self,request):
        try:
            qs = Student.objects.all()
            self.serializer = StudentSerializer(qs, many=True)
            return Response(self.serializer.data)
        except:
            return Response("Address does not exist")

    def create(self,request):
        self.request = request
        self.serializer1 = UserDetailsSerializer(data ={'username' : self.request.data['admission_number'],'password':self.request.data['parent_mobile_number'],'user_type':'2'}, context={'request': request})
        self.serializer1.is_valid(raise_exception=True)
        self.serializer1.save()
        qs = Student.objects.get(admin = self.serializer1.data['id'])
        self.request = request       
        self.serializer = StudentSerializer(instance = qs,data = self.request.data , context={'request': request})
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        return Response(self.serializer.data)

    def retrieve(self,request,pk):
        try:
            qs = Student.objects.get(pk = pk)
            self.serializer = StudentSerializer(qs)
            return Response(self.serializer.data)
        except:
            return Response(" Not exists")  

    def update(self,request,pk):
        
        try:
            qs = Student.objects.get(pk = pk)
            self.request = request       
            self.serializer = StudentSerializer(instance = qs,data = self.request.data , context={'request': request})
            self.serializer.is_valid(raise_exception=True)
            self.serializer.save()
            response = Response(self.serializer.data)
        except:
            response = Response('Oops! User does not exist', status=status.HTTP_400_BAD_REQUEST)
        return response

    def destroy(self, request, pk):
        try:
            stu = Student.objects.get(pk = pk)
            user = User.objects.get(id = stu.admin.id )
            user.delete()
            stu.delete()
            response = Response('deleted succesfully', status=status.HTTP_200_OK)
        except:
            response = Response('Oops! User does not exist', status=status.HTTP_400_BAD_REQUEST)
        return response


class TeacherDetailsView(viewsets.ViewSet):
    permission_classes = (permissions.BasePermission,)
    
    def list(self,request):
        try:
            qs = Teacher.objects.all()
            self.serializer = TeacherSerializer(qs, many=True)
            return Response(self.serializer.data)
        except:
            return Response("Address does not exist")

    def create(self,request):
        self.request = request
        self.serializer1 = UserDetailsSerializer(data ={'username' : self.request.data['mobile_number'],'password':self.request.data['mobile_number'],'user_type':'1'}, context={'request': request})
        self.serializer1.is_valid(raise_exception=True)
        self.serializer1.save()
        qs = Teacher.objects.get(admin = self.serializer1.data['id'])
        self.request = request       
        self.serializer = TeacherSerializer(instance = qs,data = self.request.data , context={'request': request})
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        return Response(self.serializer.data)

    def retrieve(self,request,pk):
        try:
            qs = Teacher.objects.get(pk = pk)
            self.serializer = TeacherSerializer(qs)
            return Response(self.serializer.data)
        except:
            return Response(" Not exists")  

    def update(self,request,pk):
        
        try:
            qs = Teacher.objects.get(pk = pk)
            self.request = request       
            self.serializer = TeacherSerializer(instance = qs,data = self.request.data , context={'request': request})
            self.serializer.is_valid(raise_exception=True)
            self.serializer.save()
            response = Response(self.serializer.data)
        except:
            response = Response('Oops! User does not exist', status=status.HTTP_400_BAD_REQUEST)
        return response

    def destroy(self, request, pk):
        try:
            teacher = Teacher.objects.get(pk = pk)
            user = User.objects.get(id = teacher.admin.id )
            user.delete()
            teacher.delete()
            response = Response('deleted succesfully', status=status.HTTP_200_OK)
        except:
            response = Response('Oops! User does not exist', status=status.HTTP_400_BAD_REQUEST)
        return response