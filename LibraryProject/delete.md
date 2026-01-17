## Delete Operation

```python
<<<<<<< HEAD
=======
from bookshelf.models import Book
>>>>>>> 5b29a6d (Complete relationship_app models and query samples)
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
