# ...existing code...
from rest_framework import serializers
from .models import Department, Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'email', 'department']

class DepartmentSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True)
    head = EmployeeSerializer(read_only=True)

    class Meta:
        model = Department
        fields = ['id', 'name', 'location', 'head', 'employees']
