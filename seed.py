from faker import Faker
from loans.models import Book

# Create 100 random books
for i in range(100):
    fake = Faker()
    author = f"{fake.last_name()}, {fake.first_name()}"
    title = fake.sentence(nb_words=4)  # A random title with 4 words
    publication_date = fake.date()
    isbn = fake.unique.isbn13().replace('-', '')

    # Create and save the Book object
    Book.objects.create(authors=author, title=title, publication_date=publication_date, isbn=isbn)

print("100 random books added to the database.")