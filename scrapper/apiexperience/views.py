from django.http import JsonResponse
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser

from .serializers import *
from rest_framework import mixins, viewsets
from django.db import connection
from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from Sector.models import ChildCompany, Company
from Worker.models import Role, Contact, Experience


################################################################


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def Experince_add(request):
    try:
        if request.method == 'POST':
            rol = None
            try:
                rol = Role.objects.get(name=request.data['roleName'])
            except:
                rol = Role.objects.create(name=request.data['roleName'],
                                          created_at=datetime.today(),
                                          updated_at=datetime.today()
                                          )

            contac = Contact.objects.create(name=request.data['contactName'],
                                            email=request.data['contactEmail'],
                                            phone=request.data['contactPhone'],
                                            about=request.data['aboutContact'],

                                            created_at=datetime.today(),
                                            updated_at=datetime.today()
                                            )

            expe = Experience.objects.create(company_id=request.data['company'],
                                             contact_id=contac.id,
                                             fromDate=request.data['fromDate'],
                                             toDate=request.data['toDate'],
                                             role_id=rol.id,

                                             created_at=datetime.today(),
                                             updated_at=datetime.today()
                                             )
        return JsonResponse({'message': 'Experience is created successfully!'}, status=status.HTTP_201_CREATED)
    except:
        return JsonResponse({'message': 'Error!'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def experience_delete(request, pk):
    try:
        expe = Experience.objects.get(pk=pk)
        expe.delete()
        return JsonResponse({'message': 'The experience was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)
    except Experience.DoesNotExist:
        return JsonResponse({'message': 'The experience does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def experience_update(request, pk):
    try:
        rol = None
        try:
            rol = Role.objects.get(name=request.data['roleName'])
        except:
            rol = Role.objects.create(name=request.data['roleName'],
                                      created_at=datetime.today(),
                                      updated_at=datetime.today()
                                      )
        try:
            contact_to_update = Contact.objects.filter(id=pk).update(name=request.data['contactName'],
                                                                     email=request.data['contactEmail'],
                                                                     phone=request.data['contactPhone'],
                                                                     about=request.data['aboutContact'],

                                                                     updated_at=datetime.today()
                                                                     )
        except:
            return JsonResponse({'message': 'The contact does not exist'}, status=status.HTTP_404_NOT_FOUND)

        try:
            experience_to_update = Experience.objects.filter(contact_id=pk).update(company_id=request.data['company'],
                                                                                   contact_id=pk,
                                                                                   fromDate=request.data['fromDate'],
                                                                                   toDate=request.data['toDate'],
                                                                                   role_id=rol.id,
                                                                                   updated_at=datetime.today()
                                                                                   )
        except Contact.DoesNotExist:
            return JsonResponse({'message': 'The Experience does not exist'}, status=status.HTTP_404_NOT_FOUND)

        return JsonResponse({'message': 'Experience is updated successfully!'}, status=status.HTTP_201_CREATED)
    except:
        return JsonResponse({'message': 'The exp does not exist'}, status=status.HTTP_404_NOT_FOUND)


class experience_detail(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = experienceSerializer
    permission_classes = [IsAuthenticated]  # this will check if it is authenticated or not
    authentication_classes = [JWTAuthentication]  # this will handel authentication automatically

    def get_object(self, queryset=None):
        obj = self.request
        return obj

    def get_queryset(self):
        getData = self.get_object()
        id = getData.GET['id']

        queryset = Experience.objects.filter(pk=id)
        # print(queryset)
        return queryset


class getAllexperienceOfCompanyViews(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = experienceSerializer
    permission_classes = [IsAuthenticated]  # this will check if it is authenticated or not
    authentication_classes = [JWTAuthentication]  # this will handel authentication automatically

    def get_object(self, queryset=None):
        obj = self.request
        return obj

    def get_queryset(self):
        getData = self.get_object()
        id = getData.GET['id']

        queryset = Experience.objects.filter(company_id=id)
        return queryset
