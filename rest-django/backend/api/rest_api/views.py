import json
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
from products.models import Product


def get_home(request):
    data = {}

    products = Product.objects.all().first()

    products = ProductSerializer(products).data

    data['products'] = products

    return Response(data)

def create_home(request):
    data = request.data
    serializer = ProductSerializer(data=data)

    if serializer.is_valid(raise_exception = True):
        serializer.save()
        data = serializer.data

        return Response(data)
    
    return Response({"error": "Invalid Data" })

@api_view(["GET", "POST"])
def home(request, *args, **kwargs):
    if request.method == 'GET':
        return get_home(request)

    if request.method == 'POST':
        return create_home(request)

    