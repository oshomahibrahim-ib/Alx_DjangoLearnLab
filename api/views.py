from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Existing ListAPIView (optional, keeps the old endpoint)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Full CRUD ViewSet
class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for all CRUD operations on Book model.
    Provides list, retrieve, create, update, delete automatically.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
