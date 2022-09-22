from django.shortcuts import HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .permissions import IsAdminorReadOnly, IsAddedByUserOrReadOnly



# Create your views here.
def home(request):
    return HttpResponse('<h1>API Page</h1>')

class StudentList(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    # permission_classes=[IsAuthenticated]
    # permission_classes=[IsAdminUser]
    # permission_classes=[IsAuthenticatedOrReadOnly]
    # permission_classes=[IsAdminorReadOnly]
    permission_classes=[IsAddedByUserOrReadOnly]


       

class StudentOperations(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()