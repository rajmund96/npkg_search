from rest_framework import serializers
from .models import Package


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['title', 'description', 'author_name', 'author_email', 'version',
                  'maintainer_email', 'maintainer_name', 'link']