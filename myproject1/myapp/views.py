# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from. models import Product
from .serializers import ProductSerializers

# Create your views here.

class ProductList(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializers(products, many=True)  #many using we fetching more than one  data
        return Response(serializer.data)
    
    def post(self,request):
        serializer=ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   #error are occure there  and bad request is used for the request is not reached there
   
class ProductDetail(APIView):
    def get(self,request,pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializers(product)
        return Response(serializer.data)

    def put(self,request,pk):
        product=Product.objects.get(pk=pk)
        serializer = ProductSerializers(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,pk):
        product=Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)