from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .serializers import UserSerializer
from .models import User

# Create your views here.
class CreateUserAPIView(APIView):
    def post(self, request):
        user_data = request.data  # 클라이언트로부터 전달받은 데이터 (사전 형태)
        print("##", user_data)
        
        # 요청 데이터를 사용하여 직렬화 객체 생성
        serializer = UserSerializer(data=user_data)
        
        # 직렬화가 유효한 경우 데이터를 저장
        if serializer.is_valid(raise_exception=True):
            serializer.save()  # 사용자 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # 성공 응답
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # 에러 응답

class GetUserAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,username):
        user_data = get_object_or_404(User,username=username)
        serializer = UserSerializer(user_data)
        return Response(serializer.data,status=status.HTTP_200_OK)