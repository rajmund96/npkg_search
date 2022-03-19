from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from .models import Package
from .serializers import PackageSerializer


class PackageViewSet(ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    http_method_names = ['get']

    filter_backends = [SearchFilter]
    search_fields = ['title', 'description', 'author_name', 'author_email', 'version',
                     'maintainer_email', 'maintainer_name']
