#from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Notification
from .serializers import NotificationSerializer



class NotificationAPIView(APIView):
    def get(self, request):
        serializer = NotificationSerializer(Notification.objects.all(),many=True)
    
        return Response(status=status.HTTP_200_OK, data=serializer.data)


    def post(self, request):
        x = request.data
        print(f"HERE-> {x}")
        data = Notification.objects.create(body=request.data['body'], email=request.data['email'],title=request.data['title'])

        
        return self.get(data)
