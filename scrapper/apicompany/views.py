from django.http import JsonResponse
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser

from .serializers import *
from rest_framework import mixins, viewsets
from django.core.files.storage import FileSystemStorage
from django.db import connection
from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from Sector.models import ChildCompany, Company, ChildCompanySector, Page


################################################################
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def Company_add(request):
    try:
        if request.method == 'POST':
            comp = None
            try:
                comp = Company.objects.get(name=request.data['campanyName'],
                                           email=request.data['email'],
                                           since=request.data['since'])
            except Company.DoesNotExist:
                comp = Company.objects.create(admin=request.user,
                                              name=request.data['campanyName'],
                                              overview=request.data['overview'],
                                              email=request.data['email'],
                                              since=request.data['since'],

                                              created_at=datetime.today(),
                                              updated_at=datetime.today()
                                              )

            chiledComp = ChildCompany.objects.create(company_id=comp.id,
                                                     city_id=request.data['city'],
                                                     nbReviews=request.data['nbReviews'],
                                                     phoneNb=request.data['phoneNb'],
                                                     ranking=request.data['ranking'],
                                                     longitude=request.data['longitude'],
                                                     latitude=request.data['latitude'],

                                                     created_at=datetime.today(),
                                                     updated_at=datetime.today()
                                                     )
            CompanySectors = request.data.getlist('sector')
            for sector in CompanySectors:
                ChildCompanySector.objects.create(child_company=chiledComp,
                                                  Sector_id=sector,
                                                  created_at=datetime.today(),
                                                  updated_at=datetime.today()
                                                  )
            Page.objects.create(company_id=comp.id,
                                url=request.data['website'],
                                created_at=datetime.today(),
                                updated_at=datetime.today()
                                )
        return JsonResponse({'message': 'Company is created successfully!'}, status=status.HTTP_201_CREATED)
    except:
        return JsonResponse({'message': 'Error!'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def childCompany_delete(request, pk):
    try:
        child = ChildCompany.objects.get(pk=pk)
        child.delete()
        return JsonResponse({'message': 'The Child Company was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)
    except ChildCompany.DoesNotExist:
        return JsonResponse({'message': 'The Child Company does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def Company_delete_with_children(request, pk):
    try:
        comp = Company.objects.get(pk=pk)
        try:
            child = ChildCompany.objects.filter(company_id=comp.id)
            for ch in child:
                ch.delete()
            comp.delete()
        except:
            pass
        return JsonResponse({'message': 'The Company with its children were deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)
    except ChildCompany.DoesNotExist:
        return JsonResponse({'message': 'The Company does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def Company_update(request, pk):
    try:
        compl = ChildCompany.objects.filter(id=pk).update(city_id=request.data['city'],
                                                          nbReviews=request.data['nbReviews'],
                                                          phoneNb=request.data['phoneNb'],
                                                          ranking=request.data['ranking'],
                                                          longitude=request.data['longitude'],
                                                          latitude=request.data['latitude'],

                                                          updated_at=datetime.today()
                                                          )

        return JsonResponse({'message': 'Child Company is updated successfully!'}, status=status.HTTP_200_OK)
    except:
        return JsonResponse({'message': 'The Child Company does not exist'}, status=status.HTTP_404_NOT_FOUND)


# @api_view(['GET'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([permissions.IsAuthenticated])
# def Company_detail(request, pk):
#     try:
#         comp = ChildCompany.objects.get(pk=pk)
#
#     except comp.DoesNotExist:
#         return JsonResponse({'message': 'The Company does not exist'}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         tutorial_serializer = ChildCompanySerializer(comp)
#         return JsonResponse(tutorial_serializer.data[0])
#

class Company_detail(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ChildCompanySerializer
    permission_classes = [IsAuthenticated]  # this will check if it is authenticated or not
    authentication_classes = [JWTAuthentication]  # this will handel authentication automatically

    def get_object(self, queryset=None):
        obj = self.request
        return obj

    def get_queryset(self):
        getData = self.get_object()
        id = getData.GET['id']

        queryset = ChildCompany.objects.filter(pk=id)
        # print(queryset)
        return queryset


class AllCompaniesViews(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ChildCompanySerializer
    permission_classes = [IsAuthenticated]  # this will check if it is authenticated or not
    authentication_classes = [JWTAuthentication]  # this will handel authentication automatically

    def get_object(self, queryset=None):
        obj = self.request
        return obj

    def get_queryset(self):
        getData = self.get_object()

        queryset = ChildCompany.objects.all()
        return queryset


class AllCompanyChildrenViews(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ChildCompanySerializer
    permission_classes = [IsAuthenticated]  # this will check if it is authenticated or not
    authentication_classes = [JWTAuthentication]  # this will handel authentication automatically

    def get_object(self, queryset=None):
        obj = self.request
        return obj

    def get_queryset(self):
        getData = self.get_object()
        id = getData.GET['id']

        queryset = ChildCompany.objects.filter(company_id=id)
        return queryset

# class MyCompaniesViews(mixins.ListModelMixin, viewsets.GenericViewSet):
#     serializer_class = ChildCompanySerializer
#     permission_classes = [IsAuthenticated]  # this will check if it is authenticated or not
#     authentication_classes = [JWTAuthentication]  # this will handel authentication automatically
#
#     def get_object(self, queryset=None):
#         obj = self.request
#         return obj
#
#     def get_queryset(self):
#         getData = self.get_object()
#
#         queryset = ChildCompanySerializer(companyId__admin=self.request.user)
#         return queryset
