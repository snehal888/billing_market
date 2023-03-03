from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Products, Invoice
from .serializers import ProductSerializer, InvoiceSerializer


class InvoiceAPI(APIView):

    def post(self, request):
        data = request.data
        return Response(data=data, status=201)
    

class ProductList(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()


class ProductDetials(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()
