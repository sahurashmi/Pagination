from rest_framework import serializers
from myapp.models import *


class StudentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Student
		fields = '__all__'
	def validate_phone(self, phone):
		phone_no = phone
		if len(str(phone_no)) != 10:
			raise serializers.ValidationError("Hey! Please be ensure phone number must be 10 digit")
		return phone
    