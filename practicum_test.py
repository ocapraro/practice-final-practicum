"""
Python unit test provided to students to test their practicum implementation.

Rather than trying to run all of the tests at once, uncomment them one at a 
time to verify that your code is working as expected.

Remember, you can select a block of code and type CTRL+/ (or Command+/) to 
comment/uncomment it.

@author Oscar Capraro
"""
from practicum import *

# PART 1 TEST
def test_create_book():
  # setup
  title = "1984"
  author = "George Orwell"
  publication_year = 1949
  compact = "1984 by George Orwell (1949)"
  detailed = "1984, a book by George Orwell, published in 1949."

  # invoke
  book = Book(title, author, publication_year)

  # analyze
  assert title == book.get_title()
  assert author == book.get_author()
  assert publication_year == book.get_publication_year()
  assert compact == str(book)
  assert detailed == repr(book)

# PART 2 TESTS
def test_sort_books():
  # setup
  book1 = Book("Adventures of Huckleberry Finn", "Mark Twain", 1884)
  book2 = Book("Iliad", "Homer", 1598)
  book3 = Book("Fahrenheit 451", "Ray Bradbury", 1953)
  book4 = Book("Dracula", "Bram Stoker", 1897)
  book5 = Book("Animal Farm", "George Orwell", 1945)
  books = [book1, book2, book3, book4, book5]

  # invoke
  copy = sorted(books)

  # analyze
  assert book4 == copy[0]
  assert book5 == copy[1]
  assert book2 == copy[2]
  assert book1 == copy[3]
  assert book3 == copy[4]

def test_sort_books_duplicates():
  # setup
  book1 = Book("Animal Farm", "George Orwell", 1945)
  book2 = Book("1984", "George Orwell", 1949)
  book3 = Book("Fahrenheit 451", "Ray Bradbury", 1953)
  book4 = Book("Adventures of Huckleberry Finn", "Mark Twain", 1884)
  book5 = Book("Iliad", "Homer", 1598)
  books = [book1, book2, book3, book4, book5]

  # invoke
  copy = sorted(books)

  # analyze
  assert book2 == copy[0]
  assert book1 == copy[1]
  assert book5 == copy[2]
  assert book4 == copy[3]
  assert book3 == copy[4]