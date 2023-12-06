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