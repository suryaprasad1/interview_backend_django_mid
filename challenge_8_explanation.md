# Challenge 8: Add Inventory Item via API (Step-by-Step Guide)

Hi 👋  
You are trying to create an API endpoint that allows you to add an Inventory item with metadata like:

- year
- actors
- imdb_rating
- rotten_tomatoes_rating
- film_locations

---

# Step 1: Create the Model

Go to `inventory_app/models.py`:
```
from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    actors = models.TextField()
    imdb_rating = models.FloatField()
    rotten_tomatoes_rating = models.FloatField()
    film_locations = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```
---

# Step 2: Run Migrations

python manage.py makemigrations
python manage.py migrate

---

# Step 3: Create Serializer

Create `inventory_app/serializers.py`:
```
from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'
```
---

# Step 4: Create API View
```
from .models import Inventory
from .serializers import InventorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class InventoryListCreateAPIView(APIView):

    # GET → list all inventory
    def get(self, request):
        items = Inventory.objects.all().order_by('id')
        serializer = InventorySerializer(items, many=True)
        return Response(serializer.data)

    # POST → create inventory item
    def post(self, request):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InventoryDetailAPIView(APIView):

    # GET single item
    def get(self, request, pk):
        try:
            item = Inventory.objects.get(pk=pk)
        except Inventory.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = InventorySerializer(item)
        return Response(serializer.data)

    # PUT → full update
    def put(self, request, pk):
        try:
            item = Inventory.objects.get(pk=pk)
        except Inventory.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = InventorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE → remove item
    def delete(self, request, pk):
        try:
            item = Inventory.objects.get(pk=pk)
        except Inventory.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
```
---

# Step 5: Add URL
```
from django.urls import path
from .views import InventoryCreateView

urlpatterns = [
    path('inventory/create/', InventoryCreateView.as_view()),
]
```
---

# Step 6: Test API

POST /inventory/create/
```
{
  "name": "Inception",
  "year": 2010,
  "actors": "Leonardo DiCaprio",
  "imdb_rating": 8.8,
  "rotten_tomatoes_rating": 87,
  "film_locations": "USA"
}
```
---

# Summary

✔ Model  
✔ Serializer  
✔ API View  
✔ URL  
