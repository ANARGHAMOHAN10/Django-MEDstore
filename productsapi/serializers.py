from rest_framework import serializers
from stores.models import Record

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Record
        fields='__all__'
