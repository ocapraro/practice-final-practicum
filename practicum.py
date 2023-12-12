"""
Implement your solution to the practicum in this file.

@author Your Name
"""
class Book:
  __slots__ = ["__title", "__author", "__publication_year"]

  def __init__(self, __title, __author, __publication_year) -> None:
    self.__title = __title
    self.__author = __author
    self.__publication_year = __publication_year

  def get_title(self) -> str:
    return self.__title
  
  def get_author(self) -> str:
    return self.__author
  
  def get_publication_year(self) -> int:
    return self.__publication_year
  
  def __str__(self) -> str:
    return self.__title + " by " + self.__author + " (" + str(self.__publication_year) + ")"
  
  def __repr__(self) -> str:
    return self.__title + ", a book by " + self.__author + ", published in " + str(self.__publication_year) + "."
  
  def __eq__(self, __o: "Book") -> bool:
    return self.__title == __o.__title and self.__author == __o.__author
  
  def __lt__(self, __o: "Book") -> bool:
    if self.__author == __o.__author:
      return self.__title < __o.__title
    return self.__author < __o.__author

class Library:
  __slots__ = ["__name", "__books"]

  def __init__(self, __name) -> None:
    self.__name = __name
    self.__books = []

  def is_empty(self) -> bool:
    return len(self.__books) == 0
  
  def reload(self, books:list[Book]) -> None:
    self.__books = books[:]
  
  def check_out(self, title:str, author:str) -> Book:
    for i in range(len(self.__books)):
      book = self.__books[i]
      if book.get_title() == title and book.get_author() == author:
        return self.__books.pop(i)
    return None
  
  def return_book(self, book:Book) -> None:
    self.__books.append(book)
  
  def get_name(self) -> str:
    return self.__name
  
  def get_books(self) -> list[Book]:
    return self.__books
  

def main():
  """
  Use this function to manually test your code (if needed)
  """

def organize_library(library:Library) -> None:
  library.get_books().sort()

def key_func(book:Book):
  return book.get_title() + book.get_author()

def organize_library_2(library:Library) -> None:
  library.get_books().sort(key=key_func)
   

if __name__ == "__main__":
  main()