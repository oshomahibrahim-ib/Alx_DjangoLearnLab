from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
author = Author.objects.get(name="George Orwell")
books_by_author = Book.objects.filter(author=author)

# Query 2: All books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()

# Query 3: Librarian for a library
librarian = Librarian.objects.get(library=library)
