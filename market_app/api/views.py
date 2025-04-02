from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from market_app.models import Manufacturer, Product, ManufacturerUser
from .serializers import ManufacturerSerializer, ProductSerializer, ManufacturerUserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsStaffOrReadOnly, IsAdminForDeleteOrPatchAndReadOnly, IsOwnerOrAdmin
# IsAdminForDeleteOrPatchAndReadOnly, IsOwnerOrAdmin     # später hinzufügen!



#@api_view(['GET'])
#@permission_classes([IsAuthenticated])
class ManufacturerList(generics.ListCreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsAuthenticated] # interne django Klasse, aber es sollte man mit decorator setzen, wie oben...
    # IsStaffOrReadOnly |
    
class ManufacturerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsAdminForDeleteOrPatchAndReadOnly]     


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ManufacturerUserList(generics.ListCreateAPIView):
    queryset = ManufacturerUser.objects.all()
    serializer_class = ManufacturerUserSerializer


class ManufacturerUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ManufacturerUser.objects.all()
    serializer_class = ManufacturerUserSerializer
    permission_classes = [IsOwnerOrAdmin]                           


class ManufacturerProductListCreate(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        manufacturer_id = self.kwargs['manufacturer_id']
        return Product.objects.filter(manufacturer_id=manufacturer_id)

    def perform_create(self, serializer):
        manufacturer_id = self.kwargs['manufacturer_id']
        serializer.save(manufacturer_id=manufacturer_id)