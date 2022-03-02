from importlib.metadata import files
from rest_framework import serializers
from rest_framework import employees
from rest_framework import projects

class employeesSerializers(serializers.ModelSerializer):

    class Meta:
        model = employees
        # filds = '__all__'
        filds = ('fistename','lastname')


class projectSerializers(serializers.ModelSerializer):

    class Meta:
        model = projects
        filds = ('projectname','projectemp')