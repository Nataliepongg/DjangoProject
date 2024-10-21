from loans.models import Book  # Import your Book model

# Delete all records from the Book model
Book.objects.all().delete()

print("All books have been removed from the database.")