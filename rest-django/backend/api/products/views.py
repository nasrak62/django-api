from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def preform_create(self, serializer):
        print(serializer)
        serializer.save()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_filed = 'pk'

    def preform_update(self, serializer):
        serializer.save()

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_filed = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


product_detail_view = ProductDetailAPIView.as_view()
product_update_view = ProductUpdateAPIView.as_view()
product_delete_view = ProductDeleteAPIView.as_view()
product_list_create_view = ProductListCreateAPIView.as_view()

@api_view(['GET','POST'])
def product_alt_view(request, pk = None, *args, **kwargs):
    method = request.method

    if method == 'POST':
        data = request.data
        serializer = ProductSerializer(data=data)

        if serializer.is_valid(raise_exception = True):
            serializer.save()
            data = serializer.data

            return Response(data)
        
        return Response({"error": "Invalid Data" })

    if method == 'GET':
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj).data
            
            return Response(data)

        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data

        return Response(data)
    if method == 'PATCH':
        pass
    if method == 'DELETE':
        pass