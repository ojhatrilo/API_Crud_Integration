from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Employee
from .serializers import EmployeeSerializer
from django.core.paginator import Paginator

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated]) # Requirement: Token-based auth 
def employee_list(request):
    if request.method == 'GET':
        # Filtering logic 
        employees = Employee.objects.all()
        dept = request.query_params.get('department')
        role = request.query_params.get('role')
        
        if dept: employees = employees.filter(department=dept)
        if role: employees = employees.filter(role=role)
        
        # Pagination is handled automatically if using Generic Views, 
        # but for FBVs, we manually apply the paginator here.

        paginator = Paginator(employees, 10)
        page_number = request.query_params.get('page')
        page_obj = paginator.get_page(page_number)
        
        serializer = EmployeeSerializer(page_obj, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def employee_detail(request, pk):
    # Retrieve single employee or return 404 
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) # [cite: 4, 5]