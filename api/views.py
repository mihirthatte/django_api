from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from django.shortcuts import render


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def home(request):
    return render(request,'index.html')

