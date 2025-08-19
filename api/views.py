# ...existing code...
from rest_framework import viewsets
from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()
        department_id = self.request.query_params.get('department')
        if department_id:
            queryset = queryset.filter(department_id=department_id)
        return queryset
