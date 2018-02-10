
class Library:
    def __init__(self,book_list):
        self.book_list=book_list
        self.book=None

    def display_books(self):
          print (" ")
          print ("Available books in the library are:")
          print (" ")
          for books in self.book_list:
            print (books)

    def lend_book(self,lended):
        if lended in self.book_list:
            print (" ")
            print ("Book is available in the library")
            self.__book_list.remove(lended)
            print (self.book_list)
            print("Thanks..You have lended a book now")
        else:
            print (" ")
            print ("Requested book not available")

    def add_book(self,added):
        print (" ")
        self.__book_list.append(added)
        print("Thanks...You have added the book now.Available books now are: ")
        print( self.book_list)

class Customer:

    def request_book(self):
        print (" ")
        print ("Enter the book you need:")
        self.requested_book = input()
        return self.requested_book

    def return_book(self):
        print (" ")
        returned_book=input("Return book name: ")
        return returned_book

book_list= ["5 Point Something","How to win and influence peaople","Bucket List","The Alchemist"]
library=Library(book_list)
customer=Customer()
while True:
    
      print (" ")
      print ("Welcome to my Library..Enjoy Reading...")
      print ("Enter 1 to display available books")
      print ("Enter 2 to request for a book")
      print ("Enter 3 to lend a book")
      print ("Enter 4 to quit")
      choice=input()
      if choice is 1:
        library.display_books()
      elif choice is 2:
        requested_book=customer.request_book()
        library.lend_book(requested_book)
      elif choice==3:
        re_book=customer.return_book()
        library.add_book(re_book)
      else:
        quit()
