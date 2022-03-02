from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employees
from .models import projects
from .serializers import employeesSerializers
from .serializers import projectSerializers
# Create your views here.


class employeeList(APIView):

    def get(self):
        employee1 = employees.objects.all()
        serializer = employeesSerializers(employee1 , many = True)
        return Response(serializer.data)

    def post(self):
        pass

class projectList(APIView):

    def get(Self):
        project1 = projects.objects.all()
        serializer = projectSerializers(project1, many = True)
        return Response(serializer.data)

    def post(self):
        pass