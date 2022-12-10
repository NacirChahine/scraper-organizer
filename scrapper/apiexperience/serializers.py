from rest_framework import serializers
# now import models from models.py
from rest_framework import serializers

from Worker.models import Experience, Contact, Role


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'name', 'email', 'phone', 'about', )


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name', )


class experienceSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(many=False)
    role = RoleSerializer(many=False)
    class Meta:
        model = Experience
        fields = ('id', 'contact', 'role', 'fromDate', 'toDate', )
        # depth = 1
