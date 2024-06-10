from rest_framework import serializers
from .models import Item, Supplier

class SupplierSerializer(serializers.ModelSerializer):
    items = serializers.StringRelatedField(many=True)

    class Meta:
        model = Supplier
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    suppliers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Item
        fields = '__all__'
