# ...existing code...
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, EmployeeViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
