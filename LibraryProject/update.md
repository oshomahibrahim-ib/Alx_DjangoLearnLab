## Update Operation

```python
<<<<<<< HEAD
=======
from bookshelf.models import Book
>>>>>>> 5b29a6d (Complete relationship_app models and query samples)
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book
