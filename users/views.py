from rest_framework import status
from .permissions import IsAdmin, IsUser
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer, UserSerializer
from rest_framework.views import APIView
import datetime

class CustomUserRegister(APIView):
    def get(self,request):
        return Response({"message":"Bu faqat POST metod uchun! Get ishlamaydi."})

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(validated_data=request.data)
            return Response({
                'status': status.HTTP_201_CREATED,
                'message': 'User created successfully',
                'data': serializer.data,
                'timestamp': datetime.datetime.now()
            })
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
        })

class CustomUserList(APIView):
    permission_classes = [IsAdmin]
    def post(self,request):
        return Response({"message":"Bu faqat GET method uchun! Post ishlamaydi."})

    def get(self,request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        serilizers_data = serializer.data
        return Response({
            'status': status.HTTP_200_OK,
            'message': "Muvaffaqqiyatli so'rov",
            'data': serilizers_data,
            'timestamp': datetime.datetime.now()
        })


class CustomUserDelete(APIView):
    permission_classes = [IsAdmin]
    def delete(self, request, id):
        try:
            user = CustomUser.objects.get(id=id)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        user.delete()
        return Response({"message": "User deleted"}, status=200)