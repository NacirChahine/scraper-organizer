from rest_framework import serializers
# now import models from models.py
from rest_framework import serializers

from Sector.models import ChildCompany


class ChildCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildCompany
        fields = '__all__'
        depth = 1
