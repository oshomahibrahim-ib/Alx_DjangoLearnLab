from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Book instances.
    Provides list, create, retrieve, update, and delete actions.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
