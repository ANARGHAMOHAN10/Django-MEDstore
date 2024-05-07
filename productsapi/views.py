
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from stores.forms import CreateRecordForm, UpdateRecordForm
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer
from productsapi.serializers import ProductSerializer
from django.shortcuts import get_object_or_404,render
from rest_framework.authentication import TokenAuthentication

from stores.models import Record

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    form = UserCreationForm(data=request.data)
    if form.is_valid():
        user = form.save()
        return Response('Account created successfully', status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt
@api_view(["POST"])
@permission_classes([AllowAny])
def logins(request):
    username=request.data.get("username")
    password=request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},status=HTTP_400_BAD_REQUEST)
    user=authenticate(username=username,password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=HTTP_200_OK)   

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_product(request):
    form = CreateRecordForm(request.POST)
    if form.is_valid():
        product = form.save()
        return Response({'id': product.id}, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])       
def list_product(request):
    products=Record.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_product(request,pk):
    product=get_object_or_404(Record,pk=pk)
    form=UpdateRecordForm(request.data,instance=product)
    if form.is_valid():
        form.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    else:
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_product(request, pk):
    try:
        product = Record.objects.get(pk=pk)
    except Record.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    product.delete()
    return Response("deleted successfully")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_product(request):
    query=request.query_params.get('query')
    if query:
        products=Record.objects.filter(medicine_name__istartswith=query)
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data)
    else:
        return Response({'error':"please provide a search query"},status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    request.auth.delete()
    return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)