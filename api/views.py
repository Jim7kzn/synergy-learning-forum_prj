from django.shortcuts import render
from .models import Checkbox
from .serializers import CheckboxSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# class CheckboxViewSet(viewsets.ModelViewSet):
#     queryset = Checkbox.objects.all()
#     serializer_class = CheckboxSerializer


@api_view(['GET'])
def checkbox_list(request):
    checkbox = Checkbox.objects.all()
    serializer = CheckboxSerializer(checkbox, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def checkbox_detail(request, pk):
    try:
        checkbox = Checkbox.objects.get(id=pk)
        serializer = CheckboxSerializer(checkbox)
    except Exception as err:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)


@api_view(['POST'])
def checkbox_create(request):
    serializer = CheckboxSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def checkbox_update(request, pk):
    try:
        checkbox = Checkbox.objects.get(id=pk)
        serializer = CheckboxSerializer(instance=checkbox, data=request.data)
        if serializer.is_valid():
            serializer.save()
    except Exception as err:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)


@api_view(['DELETE'])
def checkbox_delete(request, pk):
    # try:
    #     checkbox = Checkbox.objects.get(id=pk)
    #     serializer = CheckboxSerializer(checkbox)
    # except Exception as err:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    # return Response(serializer.data)
    checkbox = Checkbox.objects.get(id=pk)
    checkbox.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

