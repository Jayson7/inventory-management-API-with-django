from django.contrib import admin
from .models import *
# Register your models here.


all_models = [Item, Supplier]

for i in all_models:
    admin.site.register(i)