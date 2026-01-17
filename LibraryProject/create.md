<<<<<<< HEAD
## Create Operation
=======
## Create Book
>>>>>>> 5b29a6d (Complete relationship_app models and query samples)

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
