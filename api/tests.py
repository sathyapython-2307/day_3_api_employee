# ...existing code...
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Department, Employee

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.dept = Department.objects.create(name='IT', location='HQ')
        self.emp1 = Employee.objects.create(first_name='John', last_name='Doe', email='john@example.com', department=self.dept)
        self.emp2 = Employee.objects.create(first_name='Jane', last_name='Smith', email='jane@example.com', department=self.dept)
        self.dept.head = self.emp1
        self.dept.save()

    def test_create_department(self):
        response = self.client.post('/api/departments/', {'name': 'HR', 'location': 'Branch'})
        self.assertEqual(response.status_code, 201)

    def test_get_departments(self):
        response = self.client.get('/api/departments/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('employees', response.data[0])

    def test_filter_employees_by_department(self):
        response = self.client.get(f'/api/employees/?department={self.dept.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
