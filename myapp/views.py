from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from rest_framework.response import Response

from myapp.models import Student
from myapp.serializers import StudentSerializer

from myapp.pagination import CustomPagination




class StudentList(APIView):                  # inherits from an APIView
 
    def get(self, request):

        obj = Student.objects.all()
        pagination_class = CustomPagination
        paginator = pagination_class()
        
        page= paginator.paginate_queryset(obj.order_by('-id'), request)
        student_list = StudentSerializer(page, many=True)
        return paginator.get_paginated_response(student_list.data)
    

    def post(self, request):
        data = request.data             
        serializer = StudentSerializer(data=data)  
        if serializer.is_valid(raise_exception=True):

        			serializer.save()
        			return Response(serializer.data)
