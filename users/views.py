from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from  .serializers import UserRegistrationSerializer,UserSerializer
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

class RegistrationView(APIView):

    permission_classes = (AllowAny,)


    @swagger_auto_schema(responses={201:UserRegistrationSerializer},request_body=UserRegistrationSerializer)
    def post(self,request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserView(APIView):

    @swagger_auto_schema(responses={200:UserSerializer})
    def get(self,request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200:UserSerializer},request_body=UserSerializer)
    def put(self,request):
        serializer = UserSerializer(data=request.data,instance=request.user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
