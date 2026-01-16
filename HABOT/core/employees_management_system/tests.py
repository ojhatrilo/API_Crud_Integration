from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Employee

class EmployeeTests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='password123')
        # Get the token
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': 'testuser',
            'password': 'password123'
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        # Create a sample employee for testing
        self.employee = Employee.objects.create(
            name="John Doe",
            email="john@example.com",
            department="Engineering",
            role="Developer"
        )

    def test_create_employee_success(self):
        """Test creating a new employee returns 201 Created """
        data = {"name": "Jane Smith", "email": "jane@example.com"}
        response = self.client.post('/api/employees/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_duplicate_email(self):
        """Test that duplicate emails return a 400 Bad Request """
        data = {"name": "Duplicate User", "email": "john@example.com"}
        response = self.client.post('/api/employees/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_invalid_employee(self):
        """Test that non-existent IDs return 404 Not Found """
        response = self.client.get('/api/employees/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)