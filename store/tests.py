from django.test import TestCase
from rest_framework.test import APIClient
from .models import Item, Supplier

class StoreTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.supplier = Supplier.objects.create(name='Test Supplier', contact_info='Test Contact Info')
        self.item = Item.objects.create(name='Test Item', description='Test Description', price='10.00')
        self.item.suppliers.add(self.supplier)

    def test_create_item(self):
        response = self.client.post('/api/items/', {'name': 'New Item', 'description': 'New Description', 'price': '15.00'}, format='json')
        self.assertEqual(response.status_code, 201)

    def test_create_supplier(self):
        response = self.client.post('/api/suppliers/', {'name': 'Another Supplier', 'contact_info': 'Contact Info'}, format='json')
        self.assertEqual(response.status_code, 201)

    def test_get_item_suppliers(self):
        response = self.client.get(f'/api/items/{self.item.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('suppliers', response.data)

    def test_get_supplier_items(self):
        response = self.client.get(f'/api/suppliers/{self.supplier.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('items', response.data)
